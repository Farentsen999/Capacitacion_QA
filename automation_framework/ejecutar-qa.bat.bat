@echo off
title Suite de Pruebas - Francisco
echo ===========================================
echo   EJECUTANDO SUIT DE PRUEBAS
echo ===========================================

:: 1. Activar el entorno virtual desde la raíz
call venv\Scripts\activate

:: 2. Entrar a la carpeta del proyecto específico
cd automation_framework

:: 3. Ejecutar Pytest (apuntando a la carpeta de evidencias correcta)
pytest -v --headed --html=evidence/reporte_final.html --self-contained-html

:: 4. Volver a la raíz por si quieres usar otros scripts después
cd ..
echo.
echo Proceso finalizado.
pause