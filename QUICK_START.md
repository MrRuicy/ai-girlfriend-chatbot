# 快速开始指南

## 5分钟快速启动

### 1. 克隆项目
```bash
git clone https://github.com/YOUR_USERNAME/ai-girlfriend-chatbot.git
cd ai-girlfriend-chatbot
```

### 2. 安装Ollama
访问 https://ollama.ai 下载并安装

### 3. 下载模型
```bash
ollama pull qwen2.5:1.5b
```

### 4. 安装依赖
```bash
pip install -r requirements.txt
```

### 5. 配置环境
```bash
# Windows
copy env.example .env

# Linux/Mac
cp env.example .env
```

编辑 `.env` 文件：
```env
AI_PROVIDER=ollama
OLLAMA_MODEL_NAME=qwen2.5:1.5b
```

### 6. 启动应用
```bash
python main.py
```

### 7. 访问
打开浏览器访问：http://localhost:8000

**完成！开始和AI女友聊天吧！** 💕

## 使用启动脚本（更简单）

### Windows
```bash
run.bat
```

### Linux/Mac
```bash
chmod +x run.sh
./run.sh
```

## 一键配置Ollama

### Windows
```bash
setup_ollama.bat
```

### Linux/Mac
```bash
chmod +x setup_ollama.sh
./setup_ollama.sh
```

## 需要帮助？

- 查看 `README.md` 获取详细文档
- 查看 `TROUBLESHOOTING.md` 解决常见问题
- 查看 `AI_PROVIDERS_GUIDE.md` 了解AI服务配置

