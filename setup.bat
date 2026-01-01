@echo off
REM Telegram GigaChat Istanbul Guide Bot - Setup Script for Windows
REM This script creates a virtual environment and installs dependencies

echo.
echo ========================================
echo Telegram GigaChat Istanbul Guide Bot
echo Setup Script for Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment created
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo [OK] pip upgraded
echo.

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the bot, run:
echo   venv\Scripts\activate.bat
echo   python main.py
echo.
echo Make sure .env file is configured with your tokens!
echo.
pause
