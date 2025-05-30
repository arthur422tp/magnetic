# 🚀 Magentic-UI Setup Guide

This guide will help you set up Magentic-UI with secure environment variable configuration.

## 📋 Prerequisites

1. ✅ Python 3.10+ (installed in virtual environment)
2. ✅ Docker Desktop (make sure it's running)
3. ✅ Git (for version control)

## 🔧 Initial Setup

### 1. Clone and Setup Environment

```bash
# Clone the repository (if from GitHub)
git clone <your-repo-url>
cd magnetic

# Create virtual environment (if not exists)
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install magentic-ui
```

### 2. Configure Environment Variables

```bash
# Copy the template file
copy env.template .env  # Windows
# cp env.template .env    # macOS/Linux

# Edit .env file with your actual values
notepad .env  # Windows
# nano .env     # macOS/Linux
```

### 3. Fill in Your Configuration

Edit `.env` file with your actual values:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini

# Lab Configuration  
LAB_MODEL_NAME=gemma3:27b
LAB_API_URL=your_model
LAB_API_KEY=none

# Ollama Configuration
OLLAMA_MODEL=llama3
OLLAMA_URL=http://localhost:11434

# Magentic-UI Configuration
MAGENTIC_PORT=8081
```

## 🚀 Running Magentic-UI

### Option 1: Use the Launcher (Recommended)

```bash
# Double-click or run:
start_magentic_choice.bat
```

The launcher will:
1. ✅ Check if `.env` file exists
2. ✅ Generate configuration files from environment variables
3. ✅ Present you with model choices
4. ✅ Start Magentic-UI with your chosen configuration

### Option 2: Manual Generation and Start

```bash
# Generate configuration files
python generate_configs.py

# Start with specific configuration
.venv\Scripts\activate
magentic ui --port 8081 --config config.yaml          # OpenAI
magentic ui --port 8081 --config config_ollama.yaml   # Local Ollama
magentic ui --port 8081 --config config_lab_ollama.yaml # Lab
```

## 🔒 Security Features

### What's Protected:
- ✅ **API Keys**: Never committed to Git
- ✅ **URLs**: Lab and custom endpoints protected
- ✅ **Model Names**: Custom model configurations secured
- ✅ **Configuration Files**: Generated dynamically, not stored

### What's Safe to Commit:
- ✅ `env.template` - Template without real values
- ✅ `generate_configs.py` - Configuration generator script
- ✅ `start_magentic_choice.bat` - Launcher script
- ✅ Documentation files

## 📂 File Structure

```
magnetic/
├── .env                    # ❌ NOT in Git (your secrets)
├── env.template           # ✅ Safe template
├── generate_configs.py    # ✅ Config generator
├── start_magentic_choice.bat # ✅ Launcher
├── .gitignore            # ✅ Protects sensitive files
├── .venv/                # ❌ NOT in Git (Python env)
├── config.yaml           # ❌ Generated from .env
├── config_lab_ollama.yaml # ❌ Generated from .env
├── config_ollama.yaml    # ❌ Generated from .env
└── README.md             # ✅ Documentation
```

## 🔧 Troubleshooting

### "❌ Error: .env file not found!"
```bash
# Copy the template and edit it
copy env.template .env
notepad .env
```

### "❌ Failed to generate configuration files"
- Check if `.env` file has correct format
- Ensure all required variables are set
- Verify Python virtual environment is activated

### Configuration Not Working
1. Check `.env` file values
2. Regenerate configs: `python generate_configs.py`
3. Verify API keys and URLs are correct

## 🌐 For Different Environments

### Development
```env
OPENAI_MODEL=gpt-4o-mini
LAB_API_URL=your_model
```

### Production
```env
OPENAI_MODEL=gpt-4o
LAB_API_URL=https://prod-lab.yourcompany.com
```

## 🤝 Contributing

When contributing to this project:

1. ✅ **Never commit** `.env` files
2. ✅ **Always use** `env.template` for examples
3. ✅ **Update template** if you add new environment variables
4. ✅ **Test** with `generate_configs.py` before committing

---

🎉 **You're all set!** Your sensitive data is now protected and your project is ready for GitHub!

For more help, check the other documentation files or ask for assistance. 