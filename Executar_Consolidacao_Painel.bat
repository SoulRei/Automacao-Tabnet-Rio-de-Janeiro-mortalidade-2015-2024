@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "PYTHON_EXE="

rem Instalacao identificada no computador: C:\Users\LIRES\AppData\Local\Python\bin\python.exe
if exist "%LocalAppData%\Python\bin\python.exe" set "PYTHON_EXE=%LocalAppData%\Python\bin\python.exe"

rem Outras alternativas, caso o arquivo seja usado em outro computador
if not defined PYTHON_EXE if exist "%LocalAppData%\Programs\Python\Python314\python.exe" set "PYTHON_EXE=%LocalAppData%\Programs\Python\Python314\python.exe"
if not defined PYTHON_EXE if exist "%ProgramFiles%\Python314\python.exe" set "PYTHON_EXE=%ProgramFiles%\Python314\python.exe"
if not defined PYTHON_EXE (
    where py >nul 2>nul
    if not errorlevel 1 set "PYTHON_EXE=py -3.14"
)
if not defined PYTHON_EXE (
    where python >nul 2>nul
    if not errorlevel 1 set "PYTHON_EXE=python"
)

if not defined PYTHON_EXE goto nao_encontrado

echo Python localizado em: %PYTHON_EXE%
%PYTHON_EXE% Consolidar_Painel.py
if errorlevel 1 goto erro

echo.
echo Processamento concluido com sucesso.
echo Os arquivos foram criados nesta pasta.
echo.
pause
exit /b 0

:erro
echo.
echo Ocorreu um erro durante o processamento. Consulte a mensagem acima.
echo.
pause
exit /b 1

:nao_encontrado
echo Python nao foi localizado. Verifique a instalacao.
echo.
pause
exit /b 1
