# AI女友聊天机器人

一个基于FastAPI的AI女友聊天机器人，支持多种AI服务提供商，具有美观的Web界面和对话历史功能。

## 功能特点

- 💬 智能对话：支持多种AI模型（OpenAI, Ollama, Gemini, Claude等）
- 🆓 免费选项：支持Ollama本地模型，完全免费使用
- 💕 个性化角色：温柔体贴的AI女友角色设定
- 📱 微信风格UI：仿微信聊天界面，美观易用
- 👤 清纯美女头像：SVG渐变头像，视觉效果佳
- 💾 对话历史：自动保存和管理对话记录
- 🚀 易于部署：简单的配置和启动流程
- 🔄 灵活切换：支持多种AI服务提供商，随时切换
- ⚡ 轻量级：默认使用1.5B模型，速度快，资源占用少

## 🎯 快速开始（推荐使用Ollama - 完全免费）

### 方法1：使用Ollama（推荐 - 完全免费）

#### 步骤1：安装Ollama
访问 https://ollama.ai 下载并安装

#### 步骤2：下载AI模型
```bash
ollama pull qwen2.5:1.5b
```

#### 步骤3：配置环境变量
```bash
# Windows
copy env.example .env

# Linux/Mac
cp env.example .env
```

编辑 `.env` 文件，确保配置如下：
```env
AI_PROVIDER=ollama
OLLAMA_MODEL_NAME=qwen2.5:1.5b
```

#### 步骤4：安装依赖并运行
```bash
pip install -r requirements.txt
python main.py
```

#### 步骤5：访问应用
打开浏览器访问：http://localhost:8000

**完成！现在可以免费使用AI女友聊天机器人了！**

---

### 方法2：使用OpenAI API（需要付费）

#### 步骤1：安装依赖
```bash
pip install -r requirements.txt
```

#### 步骤2：配置环境变量
```bash
cp env.example .env
```

编辑 `.env` 文件：
```env
AI_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key_here
```

#### 步骤3：运行应用
```bash
python main.py
```

#### 步骤4：访问应用
打开浏览器访问：http://localhost:8000

---

## 🔄 支持的其他AI服务

### Google Gemini（有免费额度）
```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
```

### Anthropic Claude（需要付费）
```env
AI_PROVIDER=claude
CLAUDE_API_KEY=your_claude_api_key_here
```

详细配置说明请查看：`AI_PROVIDERS_GUIDE.md`

## 项目结构

```
chatbot/
├── main.py                  # 主应用入口（FastAPI应用和Web界面）
├── ai_service.py            # AI聊天服务（支持多种AI服务提供商）
├── database.py              # 数据库模型（SQLite）
├── config.py                # 配置文件
├── requirements.txt         # Python依赖包
├── env.example              # 环境变量示例文件
├── .gitignore              # Git忽略文件
├── .gitattributes          # Git属性配置
├── README.md               # 项目说明文档
├── AI_PROVIDERS_GUIDE.md   # AI服务提供商配置指南
├── TROUBLESHOOTING.md      # 故障排除指南
├── check_server.py         # 服务器状态检查工具
├── run.bat                 # Windows启动脚本
├── run.sh                  # Linux/Mac启动脚本
├── setup_ollama.bat        # Ollama配置脚本（Windows）
└── setup_ollama.sh         # Ollama配置脚本（Linux/Mac）
```

## API接口

### 聊天接口
- **URL**: `/api/chat`
- **方法**: POST
- **请求体**:
  ```json
  {
    "message": "你好",
    "user_id": "user_123"
  }
  ```
- **响应**:
  ```json
  {
    "response": "你好！很高兴认识你！",
    "user_id": "user_123"
  }
  ```

### 获取对话历史
- **URL**: `/api/history/{user_id}`
- **方法**: GET
- **响应**: 返回该用户的所有对话记录

## 自定义配置

### 修改AI角色

编辑 `config.py` 中的 `AI_GIRLFRIEND_SYSTEM_PROMPT` 来修改AI女友的性格和说话方式。

### 切换AI服务提供商

只需修改 `.env` 文件中的 `AI_PROVIDER` 即可：
- `ollama` - 免费本地模型（推荐）
- `openai` - OpenAI API
- `gemini` - Google Gemini
- `claude` - Anthropic Claude

### Ollama模型选择

推荐的中文模型：
- `qwen2.5:1.5b` - 轻量级，速度快，推荐使用（约1GB）
- `llama3.2:3b` - 轻量级，速度快（约2GB）
- `qwen2.5:7b` - 中文优秀，需要更多内存（约4.4GB）

下载模型：
```bash
ollama pull qwen2.5:1.5b
```

## 注意事项

1. **推荐使用Ollama**：完全免费，无需API密钥，数据隐私安全
2. 对话历史存储在SQLite数据库中（`chatbot.db`）
3. 如果AI服务不可用，系统会使用模拟回复（用于测试）
4. Ollama模型首次运行需要下载，请确保网络连接正常

## ❓ 常见问题

### 502错误
如果看到502错误，请检查：
1. ✅ 是否使用了正确的访问地址（localhost 或 127.0.0.1）
2. ✅ 服务器是否正在运行
3. ✅ 端口8000是否被占用

### OpenAI API错误
- 检查API密钥是否正确
- 检查API余额是否充足
- 检查网络连接

### Ollama连接失败
- 确保Ollama已安装并运行
- 检查模型是否已下载：`ollama list`
- 运行：`ollama pull qwen2.5:1.5b`

### 数据库错误
- 删除 `chatbot.db` 文件，重新启动服务器
- 检查文件权限

## 📚 更多文档

- `AI_PROVIDERS_GUIDE.md` - 详细的AI服务提供商配置指南
- `TROUBLESHOOTING.md` - 故障排除指南
- `GITHUB_SETUP.md` - GitHub仓库设置指南
- `DEPLOY.md` - 部署指南
- `CONTRIBUTING.md` - 贡献指南

## 📦 推送到GitHub

项目已准备好推送到GitHub，详细步骤请查看 `GITHUB_SETUP.md`。

**快速步骤：**
1. 在GitHub上创建新仓库
2. 配置Git用户信息（如果还没有）：
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
3. 添加远程仓库：
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   ```
4. 推送代码：
   ```bash
   git branch -M main
   git push -u origin main
   ```

## 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件了解详情

