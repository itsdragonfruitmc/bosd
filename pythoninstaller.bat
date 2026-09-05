@echo off
title Latest Python Installer
echo ==============================
echo    Installing Latest Python
echo ==============================
echo.

where winget >nul 2>&1
if %errorlevel% neq 0 (
echo Winget is not available on this PC.
echo Please install the Python installer manually from Python.org.
pause
exit /b 1
)

echo Installing Python from the official Python package...
winget install 9NQ7512CXL7 --accept-source-agreements --accept-package-agreements

echo.
echo ==============================
echo Python installation finished.
echo ==============================
python --version
pause
