@echo off
cd /d "%~dp0"
python jogo.py
if errorlevel 1 (
    echo.
    echo Se deu erro, verifique se o Python esta instalado.
    py jogo.py
)
pause
