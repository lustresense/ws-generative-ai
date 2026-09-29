@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE=python"
if exist "..\.venv\Scripts\python.exe" set "PYTHON_EXE=..\.venv\Scripts\python.exe"
if exist ".venv\Scripts\python.exe" set "PYTHON_EXE=.venv\Scripts\python.exe"

echo ============================================================
echo TUGAS 2 - MODULE 06-08
echo ============================================================
echo Python: %PYTHON_EXE%
echo.

if not exist ".env" (
    echo [ERROR] .env belum ada di folder tugas-2.
    echo Copy .env.example menjadi .env lalu isi API key dan domain 9Router.
    pause
    exit /b 1
)

echo [1/2] Running preflight...
"%PYTHON_EXE%" preflight.py
if errorlevel 1 (
    echo.
    echo Preflight gagal. Perbaiki error di atas sebelum menjalankan semua source.
    pause
    exit /b 1
)

echo.
echo [2/2] Preflight OK. Starting all 39 sources...
pause
"%PYTHON_EXE%" run_tugas_2.py --all

if errorlevel 1 (
    echo.
    echo Runner berhenti karena ada source yang gagal.
    pause
    exit /b 1
)

echo.
echo Semua source selesai.
pause
endlocal
