@echo off
title Framework de QA - Francisco

:: Cambiar al directorio donde reside este archivo .bat
cd /d "%~dp0"

echo ===========================================
echo   1. ACTIVANDO ENTORNO VIRTUAL
echo ===========================================
if exist venv\Scripts\activate (
    call venv\Scripts\activate
) else (
    echo [ERROR] No se encontro la carpeta venv. 
    echo Asegurate de que este .bat este en la misma carpeta que tu entorno virtual.
    pause
    exit
)

echo.
echo ===========================================
echo   2. EJECUTANDO TESTS Y GENERANDO REPORTE
echo ===========================================
:: Verificamos si existe la carpeta de evidencias, si no, la creamos
if not exist evidence mkdir evidence

pytest -v --headed --html=evidence/reporte_final.html --self-contained-html

echo.
echo ===========================================
echo   PROCESO TERMINADO
echo   Revisa tu reporte en: evidence/reporte_final.html
echo ===========================================
pause