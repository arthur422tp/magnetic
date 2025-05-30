# 🔬 實驗室地端模型環境變數配置指南

這個配置讓您可以安全地連接到實驗室的地端 LLM API 服務，使用環境變數管理敏感資訊。

## 🔒 環境變數配置方式

### 配置 `.env` 文件

編輯 `.env` 文件，設置實驗室相關的環境變數：

```env
# Lab Configuration
LAB_MODEL_NAME=gemma3:27b              # 您的模型名稱
LAB_API_URL=your_model     # 實驗室 API URL
LAB_API_KEY=none                       # API 金鑰 (如果需要)
```

### 自動生成配置文件

設置好環境變數後，運行：

```bash
python generate_configs.py
```

這會自動生成 `config_lab_ollama.yaml` 配置文件。

## 📝 常見實驗室配置範例

### A. 當前實驗室配置 (Ollama 格式)
```env
LAB_MODEL_NAME=gemma3:27b
LAB_API_URL=your_model
LAB_API_KEY=none
```

### B. vLLM 部署的模型
```env
LAB_MODEL_NAME=meta-llama/Llama-2-7b-chat-hf
LAB_API_URL=http://192.168.1.100:8000
LAB_API_KEY=none
```

### C. Text Generation Inference (TGI)
```env
LAB_MODEL_NAME=mistralai/Mistral-7B-Instruct-v0.1
LAB_API_URL=http://192.168.1.100:3000
LAB_API_KEY=none
```

### D. FastChat 部署
```env
LAB_MODEL_NAME=vicuna-7b-v1.5
LAB_API_URL=http://192.168.1.100:8000
LAB_API_KEY=none
```

### E. 遠端 Ollama 伺服器
```env
LAB_MODEL_NAME=llama3
LAB_API_URL=http://lab-server:11434
LAB_API_KEY=ollama
```

## 🔧 設定說明

### `LAB_MODEL_NAME` 參數
- 填入您實驗室部署的模型名稱
- 常見格式：
  - `llama3`, `mistral-7b` (簡短名稱)
  - `meta-llama/Llama-2-7b-chat-hf` (完整 HuggingFace 名稱)
  - `gemma3:27b` (帶版本的名稱)

### `LAB_API_URL` 參數  
- 您實驗室 LLM API 的基礎 URL
- 常見格式：
  - `http://伺服器IP:埠號` (內網 HTTP)
  - `https://domain.ngrok.io` (ngrok 隧道)
  - `https://lab.server.com` (正式域名)
- **注意**: 不要包含 `/v1` 後綴，腳本會自動添加

### `LAB_API_KEY` 參數
- 如果實驗室 API 需要驗證，填入提供的 API 金鑰
- 如果不需要驗證，使用 `none` 或 `dummy`
- Ollama 通常使用 `ollama` 作為 API 金鑰

## 🌐 網路設定檢查

### 1. 測試連線
```bash
# 檢查伺服器是否可達
ping dlab1.ngrok.io

# 檢查埠號是否開放 (如果是 IP:Port 格式)
telnet 192.168.1.100 8000
```

### 2. 測試 API (使用當前設置)
```bash
# 測試 Ollama 格式 API
curl -X POST "your_model/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma3:27b",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 100
  }'
```

### 3. 檢查生成的配置
```bash
# 查看生成的配置文件
type config_lab_ollama.yaml
```

## 🔐 安全性特色

### 敏感資料保護
- ✅ **API 端點 URL**: 存在 `.env` 中，不會提交到 Git
- ✅ **API 金鑰**: 如果使用自定義金鑰，受到保護
- ✅ **模型名稱**: 實驗室特定的模型配置受保護
- ✅ **動態配置**: 配置文件從環境變數即時生成

### Git 提交安全
```bash
# 檢查 Git 狀態
git status
# .env 和生成的配置文件都會被忽略
```

## 🚀 啟動方式

### 方法一：使用智能選擇器 (推薦)
```bash
# 雙擊執行或命令列運行
start_magentic_choice.bat
# 選擇選項 3 - 實驗室地端模型
```

智能啟動器會自動：
1. ✅ 檢查 `.env` 文件
2. ✅ 生成 `config_lab_ollama.yaml`
3. ✅ 啟動 Magentic-UI

### 方法二：手動操作
```bash
# 1. 生成配置
python generate_configs.py

# 2. 啟動虛擬環境
.venv\Scripts\activate

# 3. 啟動 Magentic-UI
magentic ui --port 8081 --config config_lab_ollama.yaml
```

## 🔧 疑難排解

### 環境變數相關

#### `.env` 文件未設置
```bash
# 複製模板並編輯
copy env.template .env
notepad .env
```

#### 配置生成失敗
```bash
# 檢查環境變數並重新生成
python generate_configs.py
```

### 連線相關

#### 連線錯誤
- 檢查 `LAB_API_URL` 是否正確
- 確認實驗室伺服器是否運行中
- 檢查網路連線和防火牆設定
- 確認 VPN 連線（如果需要）

#### API 調用失敗
```bash
# 檢查生成的配置內容
type config_lab_ollama.yaml

# 測試 API 端點
curl -X GET "your_model/v1/models"
```

### 模型相關

#### 模型名稱錯誤
- 確認實驗室支援的模型名稱
- 檢查 `LAB_MODEL_NAME` 設置
- 確認大小寫是否正確

#### API 格式不匹配
- 確認實驗室使用的 API 格式（OpenAI 相容 vs 原生格式）
- 檢查是否需要調整 `LAB_API_KEY` 設置

## 🔄 更新配置

### 切換實驗室環境
```bash
# 修改 .env 文件中的實驗室設置
notepad .env

# 重新生成配置
python generate_configs.py

# 重新啟動
start_magentic_choice.bat
```

### 多環境管理
您可以為不同環境創建不同的 `.env` 文件：

```bash
# 開發環境
copy .env .env.dev
# 測試環境  
copy .env .env.test
# 生產環境
copy .env .env.prod
```

## 📊 實驗室配置比較

| 部署方式 | URL 格式 | API 金鑰 | 性能 | 設置難度 |
|----------|----------|----------|------|----------|
| **當前 (Ollama)** | `your_model` | `none` | ⭐⭐⭐⭐ | ⭐ |
| **vLLM** | `http://IP:8000` | `none` | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **TGI** | `http://IP:3000` | `none` | ⭐⭐⭐⭐ | ⭐⭐ |
| **FastChat** | `http://IP:8000` | `none` | ⭐⭐⭐ | ⭐⭐⭐ |

---

## 📞 取得協助

如果遇到問題：
1. 檢查 `.env` 文件設置
2. 確認實驗室伺服器狀態
3. 聯繫實驗室管理員
4. 參考 [完整設置指南](SETUP.md)

🔬 **環境變數配置讓您的實驗室連接更安全、更靈活！** 