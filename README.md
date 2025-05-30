# Magentic-UI 環境變數配置部署

這是一個 [Microsoft Magentic-UI](https://github.com/microsoft/magentic-ui) 的本地部署版本，採用安全的環境變數配置管理。

## 🔒 環境變數配置特色

- ✅ **API 金鑰保護**: 使用 `.env` 文件，永不提交到 Git
- ✅ **多種 AI 選項**: OpenAI API, 本地 Ollama, 實驗室端點
- ✅ **自動配置生成**: 從環境變數動態產生配置檔案
- ✅ **一鍵啟動**: 智能選擇器自動檢查並啟動

## 📋 前提需求

1. ✅ Python 3.10+ (已安裝在虛擬環境中)
2. ✅ Docker Desktop (請確保正在運行)
3. ✅ AI 模型 API (OpenAI/Ollama/實驗室端點)

## 🚀 快速開始

### 1. 設置環境變數

```bash
# 複製環境變數模板
copy env.template .env

# 編輯 .env 文件
notepad .env
```

在 `.env` 文件中填入您的配置：

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini

# Lab Configuration  
LAB_MODEL_NAME=gemma3:27b
LAB_API_URL=https://dlab1.ngrok.io
LAB_API_KEY=none

# Ollama Configuration
OLLAMA_MODEL=llama3
OLLAMA_URL=http://localhost:11434

# Magentic-UI Configuration
MAGENTIC_PORT=8081
```

### 2. 一鍵啟動

```bash
# 使用智能啟動器（推薦）
start_magentic_choice.bat
```

啟動器會自動：
1. 檢查 `.env` 文件是否存在
2. 從環境變數生成配置文件
3. 提供三種 AI 模型選項
4. 啟動 Magentic-UI

### 3. 選擇 AI 模型

- **選項 1**: OpenAI API (gpt-4o-mini) - 性能最佳
- **選項 2**: 本地 Ollama (llama3) - 完全免費  
- **選項 3**: 實驗室端點 (gemma3:27b) - 客製化模型

### 4. 訪問應用程式

應用程式啟動後，在瀏覽器中訪問：
- **主要介面**: http://localhost:8081

## 🔧 手動操作

### 生成配置文件
```bash
python generate_configs.py
```

### 手動啟動特定配置
```bash
# 啟動虛擬環境
.venv\Scripts\activate

# 選擇配置啟動
magentic ui --port 8081 --config config.yaml          # OpenAI
magentic ui --port 8081 --config config_ollama.yaml   # Ollama  
magentic ui --port 8081 --config config_lab_ollama.yaml # 實驗室
```

## 🌟 功能特色

- 🌐 **Web 瀏覽代理**: 自動化網頁操作
- 💻 **程式碼生成**: AI 協助編寫和執行程式碼
- 📁 **檔案處理**: 分析和處理各種檔案格式
- 🤝 **人機協作**: 人類控制的 AI 代理系統

## 🔒 安全特性

- **敏感資料保護**: `.env` 文件已加入 `.gitignore`
- **動態配置**: 配置文件從環境變數即時生成
- **Git 友善**: 可安全提交到 GitHub 而不暴露機密
- **多環境支援**: 開發/測試/生產環境隔離

## 📂 檔案結構

```
magnetic/
├── .env                    # ❌ 您的機密資料 (不提交)
├── env.template           # ✅ 環境變數模板
├── generate_configs.py    # ✅ 配置生成器
├── start_magentic_choice.bat # ✅ 智能啟動器
├── config*.yaml          # ❌ 自動生成 (不提交)
└── .gitignore            # ✅ 保護機密檔案
```

## 🔧 疑難排解

### 環境變數相關

#### `.env` 文件未找到
```bash
# 確保已複製模板
copy env.template .env
notepad .env
```

#### 配置生成失敗
```bash
# 檢查 .env 格式是否正確
python generate_configs.py
```

### AI 模型相關

#### OpenAI API 錯誤
- 檢查 `OPENAI_API_KEY` 是否正確
- 確認 API 金鑰有足夠額度

#### Ollama 連線失敗
- 確認 Ollama 服務正在運行: `ollama serve`
- 檢查模型是否已安裝: `ollama list`

#### 實驗室端點無法訪問
- 確認 `LAB_API_URL` 是否正確
- 檢查網路連線和權限

### Docker 相關
- 確認 Docker Desktop 正在運行
- 確認 WSL 2 已啟用（Windows 用戶）

## 🌐 更多資源

- [完整設置指南](SETUP.md)
- [中文使用說明](使用說明.md)
- [Magentic-UI GitHub](https://github.com/microsoft/magentic-ui)
- [Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog/magentic-ui-an-experimental-human-centered-web-agent/)

---

🎉 **環境變數配置讓您的部署更安全、更靈活！**  
如果您需要任何協助，請隨時詢問！ 