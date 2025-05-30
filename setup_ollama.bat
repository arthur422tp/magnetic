@echo off
echo ================================================
echo   🆓 設置免費本地 LLM (Ollama) for Magentic-UI
echo ================================================

echo.
echo 步驟 1: 下載 Ollama...
echo 請訪問 https://ollama.ai/ 下載並安裝 Ollama

echo.
echo 步驟 2: 安裝推薦的模型...
echo 選擇以下其中一個命令執行：
echo.
echo   💻 程式碼導向: ollama pull codellama
echo   🌐 通用智能: ollama pull llama3
echo   ⚡ 輕量快速: ollama pull llama2
echo   🎯 平衡選擇: ollama pull mistral

echo.
echo 步驟 3: 啟動 Ollama 伺服器...
echo   ollama serve

echo.
echo 步驟 4: 使用免費配置啟動 Magentic-UI...
echo   啟動虛擬環境後執行：
echo   magentic ui --port 8081 --config config_ollama.yaml

echo.
echo ================================================
echo   完成後您就可以免費使用 Magentic-UI 了！
echo ================================================

pause 