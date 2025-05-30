#!/usr/bin/env python3
"""
Generate configuration files from environment variables
"""
import os
import sys
from pathlib import Path

def load_env_file(env_path=".env"):
    """Load environment variables from .env file"""
    env_vars = {}
    if not os.path.exists(env_path):
        print(f"❌ Error: {env_path} file not found!")
        print(f"📝 Please copy env.template to .env and fill in your values")
        return None
    
    with open(env_path, 'r', encoding='utf-8') as f:
        current_key = None
        current_value = ""
        
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line and current_key is None:
                    # New key=value pair
                    key, value = line.split('=', 1)
                    current_key = key.strip()
                    current_value = value.strip()
                    
                    # Remove quotes if present
                    if current_value.startswith('"') and current_value.endswith('"'):
                        current_value = current_value[1:-1]
                    elif current_value.startswith("'") and current_value.endswith("'"):
                        current_value = current_value[1:-1]
                    
                    # If value seems complete (doesn't end abruptly), store it
                    if not line.endswith('\\') and len(current_value) > 0:
                        env_vars[current_key] = current_value
                        current_key = None
                        current_value = ""
                elif current_key is not None:
                    # Continuation of previous value
                    current_value += line
                    # Remove quotes if this completes the value
                    if current_value.endswith('"') or current_value.endswith("'"):
                        current_value = current_value.strip('"\'')
                    env_vars[current_key] = current_value
                    current_key = None
                    current_value = ""
    
    return env_vars

def generate_openai_config(env_vars):
    """Generate OpenAI configuration"""
    config = f"""# config.yaml - Magentic-UI Configuration File
# Generated from environment variables

######################################
# Default OpenAI model configuration #
######################################
model_config: &client
  provider: autogen_ext.models.openai.OpenAIChatCompletionClient
  config:
    model: {env_vars.get('OPENAI_MODEL', 'gpt-4o-mini')}
    api_key: {env_vars.get('OPENAI_API_KEY', 'your_api_key_here')}
    max_retries: 10

##########################
# Clients for each agent #
##########################
orchestrator_client: *client
coder_client: *client
web_surfer_client: *client
file_surfer_client: *client
action_guard_client: *client"""
    
    with open('config.yaml', 'w', encoding='utf-8') as f:
        f.write(config)
    print("✅ Generated config.yaml")

def generate_lab_config(env_vars):
    """Generate Lab configuration"""
    config = f"""# config_lab_ollama.yaml - Lab Ollama API Configuration
# Generated from environment variables

######################################
# Lab Ollama API Configuration      #
######################################
model_config: &client
  provider: autogen_ext.models.openai.OpenAIChatCompletionClient
  config:
    model: {env_vars.get('LAB_MODEL_NAME', 'your_lab_model')}
    api_key: "{env_vars.get('LAB_API_KEY', 'none')}"
    base_url: "{env_vars.get('LAB_API_URL', 'your_lab_api_url')}/v1"
    max_retries: 10

##########################
# Clients for each agent #
##########################
orchestrator_client: *client
coder_client: *client
web_surfer_client: *client
file_surfer_client: *client
action_guard_client: *client"""
    
    with open('config_lab_ollama.yaml', 'w', encoding='utf-8') as f:
        f.write(config)
    print("✅ Generated config_lab_ollama.yaml")

def generate_ollama_config(env_vars):
    """Generate Ollama configuration"""
    config = f"""# config_ollama.yaml - Free Local LLM Configuration
# Generated from environment variables

######################################
# Ollama Local Model Config (Free!) #
######################################
model_config: &client
  provider: autogen_ext.models.openai.OpenAIChatCompletionClient
  config:
    model: {env_vars.get('OLLAMA_MODEL', 'llama3')}
    api_key: ollama
    base_url: {env_vars.get('OLLAMA_URL', 'http://localhost:11434')}/v1
    max_retries: 10

##########################
# Clients for each agent #
##########################
orchestrator_client: *client
coder_client: *client
web_surfer_client: *client
file_surfer_client: *client
action_guard_client: *client"""
    
    with open('config_ollama.yaml', 'w', encoding='utf-8') as f:
        f.write(config)
    print("✅ Generated config_ollama.yaml")

def main():
    print("🔧 Generating configuration files from environment variables...")
    
    # Load environment variables
    env_vars = load_env_file()
    if env_vars is None:
        sys.exit(1)
    
    # Generate configuration files
    generate_openai_config(env_vars)
    generate_lab_config(env_vars)
    generate_ollama_config(env_vars)
    
    print("🎉 All configuration files generated successfully!")
    print("💡 You can now safely commit your code without exposing sensitive data")

if __name__ == "__main__":
    main() 