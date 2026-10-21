import os
import time
import itertools
import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configurações iniciais
URL = "https://tabnet.rio.rj.gov.br/cgi-bin/dh?sim/definicoes/sim_apos2005.def"
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "Planilhas automacao")

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

chrome_options = Options()
prefs = {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

def setup_driver():
    return webdriver.Chrome(options=chrome_options)

def limpar_nome(texto):
    return texto.replace("/", "-").replace(" ", "_").replace(">", "-").replace(":", "-")

def clicar_botao_mostra(driver, wait):
    seletores = [(By.NAME, "mostre"), (By.NAME, "mostra"), (By.CSS_SELECTOR, "input[value='Mostra']")]
    for by, seletor in seletores:
        try:
            wait.until(EC.element_to_be_clickable((by, seletor))).click()
            return True
        except: continue
    raise Exception("Botão 'Mostra' não encontrado.")

def selecionar_exclusivo(driver, nome_campo, texto_opcao, valor_fallback=None):
    try:
        select_obj = Select(driver.find_element(By.NAME, nome_campo))
        select_obj.deselect_all()
        try: select_obj.select_by_visible_text(texto_opcao)
        except: select_obj.select_by_value(valor_fallback)
        return True
    except: return False

def extrair_dados():
    # CONFIGURAÇÃO DESTE SCRIPT: APENAS UM BAIRRO
    bairro_nome, bairro_val = "039 MANGUINHOS", "39"
    
    faixas_etarias = {
        "Todas as categorias": "TODAS_AS_CATEGORIAS__", "-de 1": "1", "1-4": "2", "5-9": "3", "10-14": "4", 
        "15-19": "5", "20-24": "6", "25-29": "7", "30-34": "8", "35-39": "9", "40-44": "10",
        "45-49": "11", "50-54": "12", "55-59": "13", "60-64": "14", "65-69": "15",
        "70-74": "16", "75-79": "17", "80 e+": "18", "Ign": "19"
    }
    sexos = {"Masculino": "1", "Feminino": "2"}
    racas = {
        "Todas as categorias": "TODAS_AS_CATEGORIAS__", "Branca": "1", "Preta": "2", 
        "Amarela": "3", "Parda": "4", "Indígena": "5", "Não informado": "6", "Ignorado": "7"
    }

    combinacoes = list(itertools.product(faixas_etarias.items(), sexos.items(), racas.items()))
    print(f"Iniciando Bairro: {bairro_nome} | Total: {len(combinacoes)} combinações.")

    driver = setup_driver()
    wait = WebDriverWait(driver, 25)
    wait_curto = WebDriverWait(driver, 5)

    for (f_nome, f_val), (s_nome, s_val), (r_nome, r_val) in combinacoes:
        try:
            driver.get(URL)
            wait.until(EC.presence_of_element_located((By.NAME, "Linha")))
            
            Select(driver.find_element(By.NAME, "Linha")).select_by_value("Causa_(CID10_3C)")
            Select(driver.find_element(By.NAME, "Coluna")).select_by_value("Ano_do_Óbito")
            
            select_anos = Select(driver.find_element(By.NAME, "Arquivos"))
            select_anos.deselect_all()
            for ano in range(2015, 2025):
                try: select_anos.select_by_value(f"do{str(ano)[2:]}.dbf")
                except: pass

            selecionar_exclusivo(driver, "SMunic_Resid", "330455 Rio de Janeiro", "1")
            selecionar_exclusivo(driver, "SBairro_Residencia", bairro_nome, bairro_val)
            selecionar_exclusivo(driver, "SFaixa_Etária", f_nome, f_val)
            selecionar_exclusivo(driver, "SSexo", s_nome, s_val)
            selecionar_exclusivo(driver, "SRaça/Cor", r_nome, r_val)
            
            clicar_botao_mostra(driver, wait)
            
            try:
                link_csv = wait_curto.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Copia como .CSV")))
            except TimeoutException:
                print(f"Aviso: Sem dados para {f_nome}/{s_nome}/{r_nome}. Pulando...")
                continue
            
            arquivos_antes = set(glob.glob(os.path.join(DOWNLOAD_DIR, "*.csv")))
            link_csv.click()
            
            novo_arquivo = None
            for _ in range(30):
                time.sleep(1)
                diferenca = set(glob.glob(os.path.join(DOWNLOAD_DIR, "*.csv"))) - arquivos_antes
                if diferenca:
                    novo_arquivo = list(diferenca)[0]
                    break
            
            if novo_arquivo:
                novo_nome = f"TabNet_{limpar_nome(bairro_nome)}_{limpar_nome(f_nome)}_{limpar_nome(s_nome)}_{limpar_nome(r_nome)}.csv"
                os.rename(novo_arquivo, os.path.join(DOWNLOAD_DIR, novo_nome))
                print(f"Sucesso: {novo_nome}")
            
        except Exception as e:
            print(f"Erro em {f_nome}/{s_nome}/{r_nome}: {str(e)}")
            continue

    driver.quit()

if __name__ == "__main__":
    extrair_dados()
