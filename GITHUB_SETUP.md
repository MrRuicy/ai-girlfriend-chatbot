# GitHub仓库设置指南

## 前置准备

### 配置Git用户信息

首次使用Git需要配置用户信息：

```bash
# 配置全局用户信息（推荐）
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 或者只配置当前仓库
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 验证配置

```bash
git config --list
```

## 快速开始

### 步骤1: 在GitHub上创建新仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `ai-girlfriend-chatbot`
   - **Description**: `一个基于FastAPI的AI女友聊天机器人，支持多种AI服务提供商，具有微信风格UI`
   - **Visibility**: 选择 Public 或 Private
   - **不要**勾选任何初始化选项（README、.gitignore、LICENSE）
3. 点击 "Create repository"

### 步骤2: 连接本地仓库到GitHub

复制GitHub提供的仓库URL，然后执行：

```bash
# 添加远程仓库（替换为你的仓库URL）
git remote add origin https://github.com/YOUR_USERNAME/ai-girlfriend-chatbot.git

# 或者使用SSH（推荐）
git remote add origin git@github.com:YOUR_USERNAME/ai-girlfriend-chatbot.git
```

### 步骤3: 推送代码到GitHub

```bash
# 确保你在main分支
git branch -M main

# 推送代码
git push -u origin main
```

### 步骤4: 验证

访问你的GitHub仓库页面，应该能看到所有文件已经上传。

## 后续操作

### 添加仓库描述和标签

在GitHub仓库页面：
1. 点击 "Settings" -> "General"
2. 添加详细的仓库描述
3. 添加主题标签（Topics）：`python`, `fastapi`, `ai`, `chatbot`, `ollama`, `wechat-ui`

### 添加README徽章（可选）

在README.md顶部添加：

```markdown
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
```

### 设置GitHub Pages（可选）

如果需要展示项目：
1. 在仓库设置中启用 GitHub Pages
2. 选择 main 分支作为源

## 常用Git命令

```bash
# 查看状态
git status

# 添加文件
git add .

# 提交更改
git commit -m "描述更改内容"

# 推送到GitHub
git push

# 拉取最新代码
git pull

# 查看提交历史
git log

# 创建新分支
git checkout -b feature/new-feature

# 切换分支
git checkout main
```

## 问题排查

### 如果推送失败

1. **认证问题**：
   - 使用GitHub Personal Access Token
   - 或配置SSH密钥

2. **远程仓库已存在内容**：
   ```bash
   git pull origin main --allow-unrelated-histories
   git push -u origin main
   ```

3. **权限问题**：
   - 确保你有仓库的写入权限
   - 检查GitHub账户设置

## 下一步

- 查看 `DEPLOY.md` 了解部署指南
- 查看 `CONTRIBUTING.md` 了解如何贡献代码
- 查看 `README.md` 了解项目详情

