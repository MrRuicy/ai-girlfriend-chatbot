# Git命令参考

## 📋 当前状态

项目已初始化Git仓库，所有文件已准备就绪。

## 🚀 推送到GitHub的完整命令

### 1. 配置Git用户信息（首次使用）

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. 在GitHub上创建仓库后，添加远程仓库

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### 3. 提交代码

```bash
git commit -m "Initial commit: AI女友聊天机器人

功能特点:
- 支持多种AI服务提供商（Ollama, OpenAI, Gemini, Claude）
- 微信风格UI界面，美观易用
- 轻量级本地模型（qwen2.5:1.5b），速度快
- 完整的文档和配置指南
- 跨平台支持（Windows, Linux, Mac）"
```

### 4. 重命名分支并推送

```bash
git branch -M main
git push -u origin main
```

## 📝 完整命令序列

```bash
# 1. 配置用户信息（如果还没有）
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 2. 添加远程仓库（替换为你的仓库URL）
git remote add origin https://github.com/YOUR_USERNAME/ai-girlfriend-chatbot.git

# 3. 提交代码
git commit -m "Initial commit: AI女友聊天机器人"

# 4. 推送代码
git branch -M main
git push -u origin main
```

## 🔄 后续更新命令

```bash
# 查看状态
git status

# 添加更改
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到GitHub
git push
```

## 📚 更多信息

- 详细步骤：查看 `PUSH_TO_GITHUB.md`
- GitHub设置：查看 `GITHUB_SETUP.md`
- 部署指南：查看 `DEPLOY.md`

