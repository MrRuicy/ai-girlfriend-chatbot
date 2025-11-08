"""
主应用入口
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional
import uuid

from database import init_db, get_db
from ai_service import AIChatService

# 初始化应用
app = FastAPI(title="AI女友聊天机器人")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化数据库
try:
    init_db()
    print("✅ 数据库初始化成功")
except Exception as e:
    print(f"⚠️  数据库初始化警告: {str(e)}")

# 初始化AI服务
try:
    ai_service = AIChatService()
except Exception as e:
    print(f"⚠️  AI服务初始化失败: {str(e)}")
    print("   将使用模拟回复模式")
    ai_service = None

# 请求模型
class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    user_id: str

# 根路由 - 返回前端页面
@app.get("/", response_class=HTMLResponse)
async def read_root():
    """返回聊天界面"""
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI女友聊天机器人</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
                background: #ededed;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 0;
            }
            
            .chat-container {
                width: 100%;
                max-width: 414px;
                height: 100vh;
                max-height: 896px;
                background: #ededed;
                display: flex;
                flex-direction: column;
                overflow: hidden;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
            
            .chat-header {
                background: #393a3e;
                color: white;
                padding: 12px 16px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                position: relative;
                z-index: 10;
                height: 56px;
            }
            
            .header-left {
                display: flex;
                align-items: center;
                gap: 12px;
                flex: 1;
            }
            
            .header-avatar {
                width: 40px;
                height: 40px;
                border-radius: 6px;
                overflow: hidden;
                background: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .header-avatar img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            
            .header-info {
                flex: 1;
            }
            
            .header-info h1 {
                font-size: 17px;
                font-weight: 500;
                margin-bottom: 2px;
            }
            
            .header-info .status {
                font-size: 12px;
                opacity: 0.8;
                color: #b2b2b2;
            }
            
            .chat-messages {
                flex: 1;
                overflow-y: auto;
                padding: 10px 16px;
                background: #ededed;
                scroll-behavior: smooth;
            }
            
            .chat-messages::-webkit-scrollbar {
                width: 0;
                background: transparent;
            }
            
            .message {
                margin-bottom: 10px;
                display: flex;
                align-items: flex-start;
                animation: messageSlideIn 0.2s ease-out;
            }
            
            @keyframes messageSlideIn {
                from {
                    opacity: 0;
                    transform: translateY(5px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .message.user {
                flex-direction: row-reverse;
            }
            
            .message-avatar {
                width: 40px;
                height: 40px;
                border-radius: 4px;
                flex-shrink: 0;
                overflow: hidden;
                background: #fff;
            }
            
            .message-avatar img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            
            .message.user .message-avatar {
                margin-left: 8px;
            }
            
            .message.ai .message-avatar {
                margin-right: 8px;
            }
            
            .message-wrapper {
                max-width: calc(100% - 60px);
                display: flex;
                flex-direction: column;
                position: relative;
            }
            
            .message.user .message-wrapper {
                align-items: flex-end;
            }
            
            .message.ai .message-wrapper {
                align-items: flex-start;
            }
            
            .message-content {
                padding: 10px 14px;
                word-wrap: break-word;
                word-break: break-word;
                line-height: 1.5;
                font-size: 16px;
                position: relative;
                border-radius: 4px;
            }
            
            /* 微信风格的消息气泡 */
            .message.ai .message-content {
                background: #ffffff;
                color: #191919;
                border-radius: 4px;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            }
            
            .message.ai .message-content::before {
                content: '';
                position: absolute;
                left: -6px;
                top: 12px;
                width: 0;
                height: 0;
                border-top: 6px solid transparent;
                border-bottom: 6px solid transparent;
                border-right: 6px solid #ffffff;
            }
            
            .message.user .message-content {
                background: #95ec69;
                color: #191919;
                border-radius: 4px;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            }
            
            .message.user .message-content::after {
                content: '';
                position: absolute;
                right: -6px;
                top: 12px;
                width: 0;
                height: 0;
                border-top: 6px solid transparent;
                border-bottom: 6px solid transparent;
                border-left: 6px solid #95ec69;
            }
            
            .message-time {
                font-size: 11px;
                color: #999;
                padding: 4px 0;
                text-align: center;
                width: 100%;
            }
            
            .typing-indicator {
                display: none;
                margin-bottom: 10px;
                margin-left: 48px;
            }
            
            .typing-indicator.active {
                display: flex;
                align-items: center;
            }
            
            .typing-dots {
                display: flex;
                gap: 4px;
                padding: 10px 14px;
                background: white;
                border-radius: 4px;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
                position: relative;
            }
            
            .typing-dots::before {
                content: '';
                position: absolute;
                left: -6px;
                top: 12px;
                width: 0;
                height: 0;
                border-top: 6px solid transparent;
                border-bottom: 6px solid transparent;
                border-right: 6px solid white;
            }
            
            .typing-dot {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: #999;
                animation: typing 1.4s infinite;
            }
            
            .typing-dot:nth-child(2) {
                animation-delay: 0.2s;
            }
            
            .typing-dot:nth-child(3) {
                animation-delay: 0.4s;
            }
            
            @keyframes typing {
                0%, 60%, 100% {
                    transform: translateY(0);
                    opacity: 0.7;
                }
                30% {
                    transform: translateY(-5px);
                    opacity: 1;
                }
            }
            
            .chat-input-container {
                padding: 8px;
                background: #f7f7f7;
                border-top: 1px solid #d9d9d9;
            }
            
            .chat-input-wrapper {
                display: flex;
                gap: 8px;
                align-items: flex-end;
                background: white;
                border-radius: 6px;
                padding: 6px;
            }
            
            .chat-input {
                flex: 1;
                padding: 8px 12px;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                font-family: inherit;
                outline: none;
                resize: none;
                max-height: 100px;
                line-height: 1.5;
                background: transparent;
            }
            
            .send-button {
                padding: 8px 20px;
                background: #07c160;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 15px;
                font-weight: 500;
                cursor: pointer;
                transition: background 0.2s;
                white-space: nowrap;
            }
            
            .send-button:hover:not(:disabled) {
                background: #06ad56;
            }
            
            .send-button:active:not(:disabled) {
                background: #059048;
            }
            
            .send-button:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }
            
            @media (max-width: 768px) {
                .chat-container {
                    max-width: 100%;
                    height: 100vh;
                }
                
                .message-wrapper {
                    max-width: calc(100% - 50px);
                }
            }
            
            /* 清纯美女头像样式 */
            .avatar-placeholder {
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div class="chat-container">
            <div class="chat-header">
                <div class="header-left">
                    <div class="header-avatar">
                        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="20" cy="20" r="20" fill="url(#gradient)"/>
                            <circle cx="20" cy="16" r="6" fill="white" opacity="0.9"/>
                            <path d="M8 32 C8 26, 13 22, 20 22 C27 22, 32 26, 32 32" fill="white" opacity="0.9"/>
                            <defs>
                                <linearGradient id="gradient" x1="0" y1="0" x2="40" y2="40">
                                    <stop offset="0%" stop-color="#ffecd2"/>
                                    <stop offset="100%" stop-color="#fcb69f"/>
                                </linearGradient>
                            </defs>
                        </svg>
                    </div>
                    <div class="header-info">
                        <h1>小雅</h1>
                        <div class="status">在线</div>
                    </div>
                </div>
            </div>
            <div class="chat-messages" id="chatMessages">
                <div class="message ai">
                    <div class="message-avatar">
                        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="20" cy="20" r="20" fill="url(#avatarGradient)"/>
                            <circle cx="20" cy="16" r="6" fill="white" opacity="0.95"/>
                            <path d="M8 32 C8 26, 13 22, 20 22 C27 22, 32 26, 32 32" fill="white" opacity="0.95"/>
                            <defs>
                                <linearGradient id="avatarGradient" x1="0" y1="0" x2="40" y2="40">
                                    <stop offset="0%" stop-color="#ffecd2"/>
                                    <stop offset="100%" stop-color="#fcb69f"/>
                                </linearGradient>
                            </defs>
                        </svg>
                    </div>
                    <div class="message-wrapper">
                        <div class="message-content">
                            你好！我是小雅，很高兴认识你！有什么想聊的吗？😊
                        </div>
                        <div class="message-time" id="welcomeTime"></div>
                    </div>
                </div>
            </div>
            <div class="typing-indicator" id="typingIndicator">
                <div class="typing-dots">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
            <div class="chat-input-container">
                <div class="chat-input-wrapper">
                    <textarea 
                        class="chat-input" 
                        id="chatInput" 
                        placeholder="输入消息..."
                        rows="1"
                    ></textarea>
                    <button class="send-button" onclick="sendMessage()" id="sendButton">发送</button>
                </div>
            </div>
        </div>
        
        <script>
            // 生成用户ID（如果不存在）
            let userId = localStorage.getItem('userId');
            if (!userId) {
                userId = 'user_' + Math.random().toString(36).substr(2, 9);
                localStorage.setItem('userId', userId);
            }
            
            const chatMessages = document.getElementById('chatMessages');
            const chatInput = document.getElementById('chatInput');
            const sendButton = document.getElementById('sendButton');
            const typingIndicator = document.getElementById('typingIndicator');
            
            // 设置欢迎消息的时间
            function setWelcomeTime() {
                const welcomeTime = document.getElementById('welcomeTime');
                if (welcomeTime) {
                    welcomeTime.textContent = getCurrentTime();
                }
            }
            
            // 获取当前时间
            function getCurrentTime() {
                const now = new Date();
                return now.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });
            }
            
            // 自动调整输入框高度
            function autoResizeTextarea() {
                chatInput.style.height = 'auto';
                chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + 'px';
            }
            
            // 自动滚动到底部（平滑）
            function scrollToBottom() {
                chatMessages.scrollTo({
                    top: chatMessages.scrollHeight,
                    behavior: 'smooth'
                });
            }
            
            // 添加消息到聊天界面
            function addMessage(content, isUser) {
                const messageDiv = document.createElement('div');
                messageDiv.className = 'message ' + (isUser ? 'user' : 'ai');
                
                // 创建头像
                const avatar = document.createElement('div');
                avatar.className = 'message-avatar';
                
                if (isUser) {
                    // 用户头像（简单圆形）
                    avatar.innerHTML = '<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="20" cy="20" r="20" fill="#4a90e2"/><circle cx="20" cy="16" r="6" fill="white"/><path d="M8 32 C8 26, 13 22, 20 22 C27 22, 32 26, 32 32" fill="white"/></svg>';
                } else {
                    // AI头像（清纯美女风格）
                    avatar.innerHTML = '<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="20" r="20" fill="url(#avatarGradient' + Date.now() + ')"/><circle cx="20" cy="16" r="6" fill="white" opacity="0.95"/><path d="M8 32 C8 26, 13 22, 20 22 C27 22, 32 26, 32 32" fill="white" opacity="0.95"/><defs><linearGradient id="avatarGradient' + Date.now() + '" x1="0" y1="0" x2="40" y2="40"><stop offset="0%" stop-color="#ffecd2"/><stop offset="100%" stop-color="#fcb69f"/></linearGradient></defs></svg>';
                }
                
                // 创建消息包装器
                const wrapper = document.createElement('div');
                wrapper.className = 'message-wrapper';
                
                // 创建消息内容
                const contentDiv = document.createElement('div');
                contentDiv.className = 'message-content';
                contentDiv.textContent = content;
                
                // 创建时间戳
                const timeDiv = document.createElement('div');
                timeDiv.className = 'message-time';
                timeDiv.textContent = getCurrentTime();
                
                wrapper.appendChild(contentDiv);
                wrapper.appendChild(timeDiv);
                
                messageDiv.appendChild(avatar);
                messageDiv.appendChild(wrapper);
                
                chatMessages.appendChild(messageDiv);
                scrollToBottom();
            }
            
            // 发送消息
            async function sendMessage() {
                const message = chatInput.value.trim();
                if (!message) return;
                
                // 显示用户消息
                addMessage(message, true);
                chatInput.value = '';
                autoResizeTextarea();
                
                // 禁用输入
                chatInput.disabled = true;
                sendButton.disabled = true;
                typingIndicator.classList.add('active');
                scrollToBottom();
                
                try {
                    // 发送请求到后端
                    const response = await fetch('/api/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            message: message,
                            user_id: userId
                        })
                    });
                    
                    if (!response.ok) {
                        throw new Error(`HTTP错误: ${response.status} ${response.statusText}`);
                    }
                    
                    const data = await response.json();
                    
                    // 显示AI回复
                    typingIndicator.classList.remove('active');
                    addMessage(data.response, false);
                    
                } catch (error) {
                    console.error('Error:', error);
                    typingIndicator.classList.remove('active');
                    let errorMsg = '抱歉，出现了错误，请稍后再试。';
                    if (error.message) {
                        errorMsg += ' 错误: ' + error.message;
                    }
                    addMessage(errorMsg, false);
                } finally {
                    // 恢复输入
                    chatInput.disabled = false;
                    sendButton.disabled = false;
                    chatInput.focus();
                }
            }
            
            // 输入框事件
            chatInput.addEventListener('input', autoResizeTextarea);
            
            chatInput.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendMessage();
                }
            });
            
            // 页面加载时
            window.onload = function() {
                setWelcomeTime();
                chatInput.focus();
                scrollToBottom();
            };
            
            // 定期检查并滚动到底部（防止内容加载后没有滚动）
            setInterval(function() {
                if (chatMessages.scrollHeight - chatMessages.scrollTop < chatMessages.clientHeight + 100) {
                    scrollToBottom();
                }
            }, 100);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# API路由 - 聊天接口
@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """处理聊天请求"""
    try:
        # 生成用户ID（如果未提供）
        user_id = request.user_id or str(uuid.uuid4())
        
        # 检查AI服务是否可用
        if ai_service is None:
            return ChatResponse(
                response="抱歉，AI服务暂时不可用，请检查配置后重启服务器。",
                user_id=user_id
            )
        
        # 获取对话历史
        conversation_history = ai_service.get_conversation_history(user_id)
        
        # 获取AI回复
        ai_response = ai_service.get_chat_response(
            user_message=request.message,
            user_id=user_id,
            conversation_history=conversation_history
        )
        
        return ChatResponse(response=ai_response, user_id=user_id)
        
    except Exception as e:
        import traceback
        print(f"聊天接口错误: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

# API路由 - 获取对话历史
@app.get("/api/history/{user_id}")
async def get_history(user_id: str, db: Session = Depends(get_db)):
    """获取用户对话历史"""
    try:
        if ai_service is None:
            return {
                "user_id": user_id,
                "conversations": []
            }
        conversations = ai_service.get_conversation_history(user_id)
        return {
            "user_id": user_id,
            "conversations": [
                {
                    "message": conv.message,
                    "response": conv.response,
                    "created_at": conv.created_at.isoformat()
                }
                for conv in conversations
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 健康检查
@app.get("/health")
async def health():
    """健康检查"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("🚀 AI女友聊天机器人启动中...")
    print("=" * 50)
    print(f"📍 本地访问地址: http://localhost:8000")
    print(f"📍 网络访问地址: http://127.0.0.1:8000")
    print("=" * 50)
    print("⚠️  注意: 请不要直接访问 0.0.0.0，请使用 localhost 或 127.0.0.1")
    print("=" * 50)
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    except Exception as e:
        print(f"❌ 启动失败: {str(e)}")
        print("请检查端口8000是否被占用，或查看上面的错误信息")

