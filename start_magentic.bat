@echo off
echo 正在啟動 Magentic-UI...
echo 請確保 Docker Desktop 正在運行中

REM 啟動虛擬環境
call .venv\Scripts\activate

REM 啟動 magentic-ui，使用配置檔案
echo 正在啟動 Magentic-UI 在 port 8081...
magentic ui --port 8081 --config config.yaml

pause 