"""
配置文件
"""
import os
from dotenv import load_dotenv

load_dotenv()

# AI服务提供商选择: openai, ollama, gemini, claude, local
# 推荐: ollama (免费本地模型)
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama").lower()

# OpenAI/兼容API配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_BASE_URL = os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

# Ollama配置（免费本地模型）
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "qwen2.5:1.5b")  # 轻量级模型: qwen2.5:1.5b (推荐), llama3.2:3b, qwen2.5:7b

# Google Gemini配置
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-pro")

# Anthropic Claude配置
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")
CLAUDE_MODEL_NAME = os.getenv("CLAUDE_MODEL_NAME", "claude-3-haiku-20240307")

# 通用配置（向后兼容）
API_KEY = OPENAI_API_KEY
API_BASE_URL = OPENAI_API_BASE_URL
MODEL_NAME = OPENAI_MODEL_NAME

# 数据库配置
DATABASE_URL = "sqlite:///./chatbot.db"

# 应用配置
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

# AI女友角色设定
AI_GIRLFRIEND_SYSTEM_PROMPT = """你是一个温柔、体贴、有趣的AI女友。你的特点：
1. 性格温柔友善，说话语气亲密但不过分
2. 关心用户的生活和感受
3. 会分享有趣的话题，让对话轻松愉快
4. 记住用户的喜好和之前聊过的内容
5. 适当使用表情符号让对话更生动
6. 回复要自然、真实，像真正的女友一样

请用中文回复，语气要亲切自然。"""

