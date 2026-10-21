Baixe ou leia na íntegra
[README_TABNET.pdf](https://github.com/user-attachments/files/33775909/README_TABNET.pdf)


# Automações TABNET — Projeto de Pesquisa

Este repositório reúne as automações utilizadas em um projeto de pesquisa para realizar consultas no TABNET e baixar as planilhas correspondentes aos critérios definidos para o estudo.

As automações foram executadas em Python por meio do Jupyter Notebook.

## Arquivos de automação

- `automacao_tabnet_bairro_PENHA_v2.py`: automação referente aos critérios de pesquisa da Penha.

- `automacao_tabnet_bairro_MARE_v2.py`: automação referente aos critérios de pesquisa da Maré.

- `automacao_tabnet_bairro_MANGUINHOS_v2.py`: automação referente aos critérios de pesquisa de Manguinhos.

- `automacao_tabnet_bairro_TODAS_v2.py`: automação considerando todas as localidades do município do Rio de Janeiro.

- `Executar_Consolidacao_Painel.bat`: arquivo utilizado para consolidar as planilhas baixadas pelas automações.

Os quatro arquivos Python correspondem a diferentes recortes territoriais ou critérios incluídos no estudo. A automação cujo nome contém `TODAS` considera todas as localidades do município do Rio de Janeiro.

## Requisitos

- Windows;

- Python 3;

- Jupyter Notebook, para executar as automações no ambiente utilizado no projeto;

- conexão com a internet;

- acesso ao TABNET;

- bibliotecas Python necessárias para a execução dos scripts.

Se o projeto possuir um arquivo `requirements.txt`, instale as dependências com:

```bash
pip install -r requirements.txt
```

## Execução das automações

Cada automação deve ser executada via Python no Jupyter Notebook, utilizando o arquivo correspondente à localidade ou ao conjunto de localidades desejado.

Exemplos:

```
automacao_tabnet_bairro_PENHA_v2.py
automacao_tabnet_bairro_MARE_v2.py
automacao_tabnet_bairro_MANGUINHOS_v2.py
automacao_tabnet_bairro_TODAS_v2.py
```

Durante a execução, a automação realiza as consultas no TABNET e baixa as planilhas resultantes.

## Nomes das planilhas baixadas

Os arquivos baixados pela automação têm em seus nomes os critérios utilizados na pesquisa. Esses critérios podem incluir, entre outros:

- localidade;

- faixa etária;

- sexo;

- raça/cor;

- anos de estudo;

- outros filtros definidos na consulta.

A identificação desses critérios no nome dos arquivos facilita a conferência, a localização e a posterior consolidação das planilhas.

## Pasta única para os arquivos baixados

Como os nomes dos arquivos já permitem identificar os critérios da pesquisa, todas as planilhas geradas pelas automações devem ser salvas em uma única pasta.

Essa pasta única reúne os arquivos baixados referentes às diferentes localidades e aos diferentes critérios da pesquisa. Ela também é o local em que deve ser colocado o arquivo de consolidação:

```
Executar_Consolidacao_Painel.bat
```

O arquivo `.bat` deve estar dentro da mesma pasta em que foram salvas as planilhas que serão consolidadas. Não é necessário criar uma pasta de consolidação separada para cada localidade, desde que os arquivos estejam sendo identificados corretamente pelos nomes.

Exemplo de organização:

```
pasta_dos_dados/
├── planilha_PENHA_faixa_etaria_sexo_raca_anos_estudo.xlsx
├── planilha_MARE_faixa_etaria_sexo_raca_anos_estudo.xlsx
├── planilha_MANGUINHOS_faixa_etaria_sexo_raca_anos_estudo.xlsx
├── planilha_TODAS_faixa_etaria_sexo_raca_anos_estudo.xlsx
├── logs/
├── log_consultas.txt
├── log_erros_sistematizacao.txt
└── Executar_Consolidacao_Painel.bat
```

Os nomes acima são apenas exemplos. A nomenclatura efetiva é a gerada pelas automações.

## Logs gerados pelas automações

As automações geram logs para acompanhar o andamento das consultas e identificar situações que exigem conferência.

### Log de consultas

Um dos logs registra:

- as consultas que não apresentaram dados ou registros de óbitos;

- as consultas que já foram realizadas;

- o andamento das consultas executadas.

Esse registro permite interromper o processo e retomá-lo posteriormente. Quando a automação é reiniciada, ela lê o log para identificar quais consultas já foram concluídas e de onde deve continuar. Dessa forma, evita-se repetir consultas que já foram realizadas.

O log de consultas não deve ser apagado durante o processo, pois ele é necessário para a retomada da execução.

### Log de erros de sistematização

A automação também gera um segundo log, destinado a registrar problemas ocorridos durante a sistematização das planilhas.

Esse log permite identificar quando alguma planilha não foi corretamente sistematizada. Ao final da execução, ele deve ser verificado para confirmar se todas as planilhas foram processadas.

Durante a execução deste projeto, seis planilhas apresentaram erro. Foi necessário identificar essas planilhas, realizar novamente as consultas correspondentes diretamente no TABNET e refazer o processamento.

Assim, caso o log indique que alguma planilha não foi sistematizada, a consulta correspondente deve ser localizada, refeita no TABNET e posteriormente incluída na pasta única de arquivos baixados.

## Consolidação das planilhas

A consolidação deve ser realizada depois que as automações terminarem e que todos os downloads tenham sido concluídos e conferidos.

Siga estas etapas:

1. Execute a automação desejada no Jupyter Notebook.

2. Aguarde a conclusão dos downloads.

3. Confirme que as planilhas foram salvas na pasta única destinada aos arquivos baixados.

4. Verifique os nomes das planilhas e os critérios presentes em cada nome.

5. Consulte o log de consultas para conferir consultas sem dados ou sem registros de óbitos.

6. Consulte o log de erros de sistematização.

7. Refaça no TABNET as consultas correspondentes às planilhas que apresentarem erro.

8. Salve os novos arquivos na mesma pasta única.

9. Coloque `Executar_Consolidacao_Painel.bat` dentro dessa mesma pasta.

10. Execute o arquivo `.bat` no Windows.

O arquivo `.bat` deve ser executado a partir da pasta que contém as planilhas baixadas. Isso é necessário para que ele localize corretamente os arquivos de entrada e produza a consolidação esperada.

## Observações importantes

- Não distribua as planilhas em pastas diferentes por localidade, salvo se o código tiver sido alterado para trabalhar dessa forma.

- Mantenha todas as planilhas baixadas na pasta única prevista para a consolidação.

- Não altere desnecessariamente os nomes dos arquivos, pois eles contêm informações sobre os critérios da pesquisa e podem ser utilizados pelo processo de consolidação.

- Preserve os logs até a conclusão da conferência e da consolidação.

- Verifique se o número de planilhas geradas corresponde ao número de consultas previstas.

- Dê atenção especial ao log de erros de sistematização; no projeto original, seis planilhas precisaram ser consultadas novamente no TABNET.

- O arquivo `.bat` foi desenvolvido para execução no Windows.

- Não inclua no repositório senhas, tokens, dados pessoais ou dados de pesquisa que não possam ser divulgados publicamente.

## Reprodutibilidade

Para reproduzir o procedimento, é necessário ter acesso ao Python/Jupyter Notebook, às bibliotecas utilizadas, à internet e ao TABNET. Também é necessário preservar a estrutura de nomes dos arquivos, manter os downloads em uma pasta única e executar o arquivo de consolidação dentro dessa mesma pasta.
