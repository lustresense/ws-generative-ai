@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE=python"
if exist "..\.venv\Scripts\python.exe" set "PYTHON_EXE=..\.venv\Scripts\python.exe"
if exist ".venv\Scripts\python.exe" set "PYTHON_EXE=.venv\Scripts\python.exe"

echo ============================================================
echo TUGAS 2 - RUN ONE BY ONE (CLEAN TERMINAL MODE)
echo ============================================================
echo Python: %PYTHON_EXE%
echo.

if not exist ".env" (
    echo [ERROR] .env belum ada di folder tugas-2.
    pause
    exit /b 1
)

"%PYTHON_EXE%" run_one_by_one.py

echo.
pause
endlocal
