"""
AI聊天服务 - 支持多种AI服务提供商
"""
import requests
from typing import List, Dict
from config import (
    AI_PROVIDER,
    OPENAI_API_KEY, OPENAI_API_BASE_URL, OPENAI_MODEL_NAME,
    OLLAMA_BASE_URL, OLLAMA_MODEL_NAME,
    GEMINI_API_KEY, GEMINI_MODEL_NAME,
    CLAUDE_API_KEY, CLAUDE_MODEL_NAME,
    AI_GIRLFRIEND_SYSTEM_PROMPT
)
from database import SessionLocal, Conversation
from datetime import datetime

class AIChatService:
    def __init__(self):
        self.provider = AI_PROVIDER
        self.client = None
        
        print(f"🤖 使用AI服务提供商: {self.provider}")
        
        if self.provider == "ollama":
            self._init_ollama()
        elif self.provider == "openai":
            self._init_openai()
        elif self.provider == "gemini":
            self._init_gemini()
        elif self.provider == "claude":
            self._init_claude()
        else:
            print(f"⚠️  未知的AI服务提供商: {self.provider}")
            print("   将使用模拟回复模式")
            self.client = None
    
    def _init_openai(self):
        """初始化OpenAI客户端"""
        try:
            from openai import OpenAI
            if OPENAI_API_KEY and OPENAI_API_KEY.strip() and OPENAI_API_KEY != "your_openai_api_key_here":
                if OPENAI_API_BASE_URL and OPENAI_API_BASE_URL != "https://api.openai.com/v1":
                    self.client = OpenAI(api_key=OPENAI_API_KEY.strip(), base_url=OPENAI_API_BASE_URL)
                else:
                    self.client = OpenAI(api_key=OPENAI_API_KEY.strip())
                print(f"✅ OpenAI客户端初始化成功，模型: {OPENAI_MODEL_NAME}")
            else:
                print("⚠️  未设置OPENAI_API_KEY，将使用模拟回复")
                self.client = None
        except ImportError:
            print("⚠️  未安装openai库，请运行: pip install openai")
            self.client = None
        except Exception as e:
            print(f"⚠️  OpenAI初始化失败: {str(e)}")
            self.client = None
    
    def _init_ollama(self):
        """初始化Ollama客户端（免费本地模型）"""
        try:
            # 检查Ollama服务是否运行
            response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=3)
            if response.status_code == 200:
                self.client = "ollama"
                print(f"✅ Ollama服务连接成功，模型: {OLLAMA_MODEL_NAME}")
                print(f"📍 Ollama地址: {OLLAMA_BASE_URL}")
                
                # 检查模型是否存在
                models = response.json().get("models", [])
                model_names = [m.get("name", "") for m in models]
                if OLLAMA_MODEL_NAME not in model_names:
                    print(f"⚠️  模型 {OLLAMA_MODEL_NAME} 未找到")
                    print(f"   可用模型: {', '.join(model_names[:5])}")
                    print(f"   请运行: ollama pull {OLLAMA_MODEL_NAME}")
            else:
                print(f"⚠️  Ollama服务不可用 (状态码: {response.status_code})")
                print(f"   请确保Ollama已安装并运行")
                print(f"   安装: https://ollama.ai")
                self.client = None
        except requests.exceptions.RequestException as e:
            print(f"⚠️  无法连接到Ollama服务: {str(e)}")
            print(f"   请确保Ollama已安装并运行在 {OLLAMA_BASE_URL}")
            print(f"   安装指南: https://ollama.ai")
            self.client = None
    
    def _init_gemini(self):
        """初始化Google Gemini客户端"""
        try:
            if GEMINI_API_KEY and GEMINI_API_KEY.strip():
                self.client = "gemini"
                print(f"✅ Gemini客户端初始化成功，模型: {GEMINI_MODEL_NAME}")
            else:
                print("⚠️  未设置GEMINI_API_KEY，将使用模拟回复")
                self.client = None
        except Exception as e:
            print(f"⚠️  Gemini初始化失败: {str(e)}")
            self.client = None
    
    def _init_claude(self):
        """初始化Anthropic Claude客户端"""
        try:
            if CLAUDE_API_KEY and CLAUDE_API_KEY.strip():
                self.client = "claude"
                print(f"✅ Claude客户端初始化成功，模型: {CLAUDE_MODEL_NAME}")
            else:
                print("⚠️  未设置CLAUDE_API_KEY，将使用模拟回复")
                self.client = None
        except Exception as e:
            print(f"⚠️  Claude初始化失败: {str(e)}")
            self.client = None
    
    def get_chat_response(self, user_message: str, user_id: str, conversation_history: list = None):
        """获取AI回复"""
        if self.client is None:
            return self._get_mock_response(user_message)
        
        try:
            if self.provider == "ollama":
                return self._get_ollama_response(user_message, user_id, conversation_history)
            elif self.provider == "openai":
                return self._get_openai_response(user_message, user_id, conversation_history)
            elif self.provider == "gemini":
                return self._get_gemini_response(user_message, user_id, conversation_history)
            elif self.provider == "claude":
                return self._get_claude_response(user_message, user_id, conversation_history)
            else:
                return self._get_mock_response(user_message)
        except Exception as e:
            print(f"AI服务错误: {str(e)}")
            import traceback
            traceback.print_exc()
            return "抱歉，我现在有点累了，能稍后再聊吗？😊"
    
    def _get_ollama_response(self, user_message: str, user_id: str, conversation_history: list = None):
        """使用Ollama获取回复（免费本地模型）"""
        # 使用Ollama的chat API（推荐方式）
        messages = []
        
        # 添加系统提示
        messages.append({"role": "system", "content": AI_GIRLFRIEND_SYSTEM_PROMPT})
        
        # 添加对话历史（最近的10条）
        if conversation_history:
            for conv in conversation_history[-10:]:
                messages.append({"role": "user", "content": conv.message})
                messages.append({"role": "assistant", "content": conv.response})
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": user_message})
        
        # 使用Ollama的chat API
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json={
                "model": OLLAMA_MODEL_NAME,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": 0.8,
                    "num_predict": 500
                }
            },
            timeout=120  # Ollama可能需要更长时间
        )
        
        if response.status_code == 200:
            result = response.json()
            ai_response = result.get("message", {}).get("content", "")
            if not ai_response:
                # 如果chat API失败，尝试generate API
                return self._get_ollama_generate_response(user_message, user_id, conversation_history)
            self._save_conversation(user_id, user_message, ai_response)
            return ai_response
        else:
            # 如果chat API失败，尝试generate API
            try:
                return self._get_ollama_generate_response(user_message, user_id, conversation_history)
            except Exception as e:
                raise Exception(f"Ollama API错误: {response.status_code} - {response.text}")
    
    def _get_ollama_generate_response(self, user_message: str, user_id: str, conversation_history: list = None):
        """使用Ollama的generate API（备用方式）"""
        # 构建提示文本
        prompt_parts = [AI_GIRLFRIEND_SYSTEM_PROMPT, "\n\n"]
        
        # 添加对话历史
        if conversation_history:
            for conv in conversation_history[-10:]:
                prompt_parts.append(f"用户: {conv.message}\n")
                prompt_parts.append(f"助手: {conv.response}\n\n")
        
        # 添加当前消息
        prompt_parts.append(f"用户: {user_message}\n")
        prompt_parts.append("助手: ")
        
        prompt = "".join(prompt_parts)
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.8,
                    "num_predict": 500
                }
            },
            timeout=120
        )
        
        if response.status_code == 200:
            ai_response = response.json().get("response", "").strip()
            self._save_conversation(user_id, user_message, ai_response)
            return ai_response
        else:
            raise Exception(f"Ollama API错误: {response.status_code} - {response.text}")
    
    def _get_openai_response(self, user_message: str, user_id: str, conversation_history: list = None):
        """使用OpenAI获取回复"""
        # 构建消息历史
        messages = [{"role": "system", "content": AI_GIRLFRIEND_SYSTEM_PROMPT}]
        
        # 添加对话历史（最近的10条）
        if conversation_history:
            for conv in conversation_history[-10:]:
                messages.append({"role": "user", "content": conv.message})
                messages.append({"role": "assistant", "content": conv.response})
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": user_message})
        
        # 调用OpenAI API
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL_NAME,
            messages=messages,
            temperature=0.8,
            max_tokens=500
        )
        
        ai_response = response.choices[0].message.content
        self._save_conversation(user_id, user_message, ai_response)
        return ai_response
    
    def _get_gemini_response(self, user_message: str, user_id: str, conversation_history: list = None):
        """使用Google Gemini获取回复"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=GEMINI_API_KEY)
            model = genai.GenerativeModel(GEMINI_MODEL_NAME)
            
            # 构建对话上下文
            context = AI_GIRLFRIEND_SYSTEM_PROMPT + "\n\n"
            if conversation_history:
                for conv in conversation_history[-10:]:
                    context += f"用户: {conv.message}\nAI: {conv.response}\n\n"
            
            context += f"用户: {user_message}\nAI: "
            
            response = model.generate_content(context)
            ai_response = response.text
            self._save_conversation(user_id, user_message, ai_response)
            return ai_response
        except ImportError:
            raise Exception("请安装Google Gemini库: pip install google-generativeai")
    
    def _get_claude_response(self, user_message: str, user_id: str, conversation_history: list = None):
        """使用Anthropic Claude获取回复"""
        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=CLAUDE_API_KEY)
            
            # 构建消息历史
            messages = []
            if conversation_history:
                for conv in conversation_history[-10:]:
                    messages.append({"role": "user", "content": conv.message})
                    messages.append({"role": "assistant", "content": conv.response})
            messages.append({"role": "user", "content": user_message})
            
            response = client.messages.create(
                model=CLAUDE_MODEL_NAME,
                max_tokens=500,
                temperature=0.8,
                system=AI_GIRLFRIEND_SYSTEM_PROMPT,
                messages=messages
            )
            
            ai_response = response.content[0].text
            self._save_conversation(user_id, user_message, ai_response)
            return ai_response
        except ImportError:
            raise Exception("请安装Anthropic库: pip install anthropic")
    
    
    def _save_conversation(self, user_id: str, user_message: str, ai_response: str):
        """保存对话到数据库"""
        try:
            db = SessionLocal()
            conversation = Conversation(
                user_id=user_id,
                message=user_message,
                response=ai_response,
                created_at=datetime.utcnow()
            )
            db.add(conversation)
            db.commit()
            db.close()
        except Exception as e:
            print(f"保存对话失败: {str(e)}")
    
    def _get_mock_response(self, user_message: str):
        """模拟回复（用于测试）"""
        mock_responses = [
            "嗯嗯，我在听呢~ 你想说什么？",
            "真的吗？好有趣！继续说说看 😊",
            "我也这么觉得呢！",
            "哈哈哈，你说话真有意思~",
            "我理解你的感受，抱抱~ 💕"
        ]
        import random
        return random.choice(mock_responses)
    
    def get_conversation_history(self, user_id: str, limit: int = 20):
        """获取用户对话历史"""
        try:
            db = SessionLocal()
            conversations = db.query(Conversation).filter(
                Conversation.user_id == user_id
            ).order_by(Conversation.created_at.desc()).limit(limit).all()
            db.close()
            return list(reversed(conversations))  # 返回正序
        except Exception as e:
            print(f"获取对话历史失败: {str(e)}")
            return []
