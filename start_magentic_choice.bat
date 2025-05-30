@echo off
title Magentic-UI Launcher
color 0A

echo ================================================
echo          🤖 Magentic-UI Launcher
echo ================================================
echo.

REM Check if .env file exists
if not exist ".env" (
    echo ❌ Error: .env file not found!
    echo.
    echo 📝 Please follow these steps:
    echo    1. Copy env.template to .env
    echo    2. Edit .env and fill in your API keys and URLs
    echo    3. Run this script again
    echo.
    pause
    exit /b 1
)

echo 🔧 Generating configuration files from .env...
call .venv\Scripts\activate
python generate_configs.py

if %ERRORLEVEL% neq 0 (
    echo ❌ Failed to generate configuration files
    pause
    exit /b 1
)

echo.
echo Please choose your AI model source:
echo.
echo   1. 🌐 OpenAI API (GPT-4o-mini) - Paid, Best Performance
echo   2. 🏠 Local Model (Ollama) - Free, Privacy Protection  
echo   3. 🔬 Lab Model (Ollama Format) - Lab Custom Model
echo.
echo   0. ❌ Cancel
echo.
echo ================================================

set /p choice="Please enter option (1-3): "

if "%choice%"=="1" goto openai
if "%choice%"=="2" goto ollama  
if "%choice%"=="3" goto lab_ollama
if "%choice%"=="0" goto exit
goto invalid

:openai
echo.
echo 🌐 Starting OpenAI version...
echo Make sure you have set your API key in .env file
echo.
magentic ui --port 8081 --config config.yaml
goto end

:ollama
echo.
echo 🏠 Starting local model version...
echo Make sure Ollama service is running (ollama serve)
echo.
magentic ui --port 8081 --config config_ollama.yaml
goto end

:lab_ollama
echo.
echo 🔬 Starting lab model version (Ollama Format)...
echo Reading configuration from .env file...
echo.
magentic ui --port 8081 --config config_lab_ollama.yaml
goto end

:invalid
echo.
echo ❌ Invalid option, please try again
echo.
pause
cls
goto start

:exit
echo.
echo 👋 Cancelled
goto end

:end
echo.
echo If you encounter problems, please check your .env file and configuration
pause 