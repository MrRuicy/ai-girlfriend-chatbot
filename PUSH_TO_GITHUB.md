# 推送到GitHub - 完整指南

## 📋 前置检查清单

- [ ] Git已安装
- [ ] GitHub账户已创建
- [ ] Git用户信息已配置

## 🚀 完整步骤

### 步骤1: 配置Git用户信息（首次使用）

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

验证配置：
```bash
git config --list
```

### 步骤2: 在GitHub上创建仓库

1. 登录GitHub
2. 点击右上角 "+" → "New repository"
3. 填写信息：
   - **Repository name**: `ai-girlfriend-chatbot`
   - **Description**: `一个基于FastAPI的AI女友聊天机器人，支持多种AI服务提供商，具有微信风格UI`
   - **Visibility**: Public 或 Private
   - **不要**勾选任何初始化选项
4. 点击 "Create repository"

### 步骤3: 连接本地仓库

```bash
# 添加远程仓库（替换为你的仓库URL）
git remote add origin https://github.com/YOUR_USERNAME/ai-girlfriend-chatbot.git

# 或者使用SSH（推荐，需要配置SSH密钥）
git remote add origin git@github.com:YOUR_USERNAME/ai-girlfriend-chatbot.git
```

验证远程仓库：
```bash
git remote -v
```

### 步骤4: 提交代码

```bash
# 查看状态
git status

# 添加所有文件
git add .

# 创建提交
git commit -m "Initial commit: AI女友聊天机器人

- 支持多种AI服务提供商（Ollama, OpenAI, Gemini, Claude）
- 微信风格UI界面
- 轻量级本地模型（qwen2.5:1.5b）
- 完整的文档和配置指南"

# 重命名分支为main（如果需要）
git branch -M main
```

### 步骤5: 推送到GitHub

```bash
# 首次推送
git push -u origin main

# 后续推送
git push
```

### 步骤6: 验证

访问你的GitHub仓库页面：`https://github.com/YOUR_USERNAME/ai-girlfriend-chatbot`

应该能看到所有文件已经上传。

## 🔧 常见问题

### 问题1: 认证失败

**解决方案：**
- 使用GitHub Personal Access Token
- 或配置SSH密钥

**使用Token：**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 生成新token，勾选 `repo` 权限
3. 使用token作为密码

**配置SSH：**
```bash
# 生成SSH密钥
ssh-keygen -t ed25519 -C "your.email@example.com"

# 添加到SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 复制公钥
cat ~/.ssh/id_ed25519.pub

# 添加到GitHub: Settings → SSH and GPG keys → New SSH key
```

### 问题2: 远程仓库已存在内容

如果远程仓库已经有内容（如README），需要先拉取：

```bash
git pull origin main --allow-unrelated-histories
# 解决可能的冲突
git push -u origin main
```

### 问题3: 权限被拒绝

确保：
- GitHub账户有仓库的写入权限
- 使用正确的仓库URL
- SSH密钥已正确配置

## 📝 后续维护

### 更新代码

```bash
# 查看更改
git status

# 添加更改
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到GitHub
git push
```

### 创建分支

```bash
# 创建新分支
git checkout -b feature/new-feature

# 切换分支
git checkout main

# 合并分支
git merge feature/new-feature
```

### 查看历史

```bash
# 查看提交历史
git log

# 查看简洁历史
git log --oneline

# 查看文件更改
git diff
```

## 🎉 完成！

你的项目现在已经推送到GitHub了！

下一步：
- 添加仓库描述和标签
- 设置GitHub Pages（如果需要）
- 添加README徽章
- 邀请协作者

查看 `GITHUB_SETUP.md` 了解更多GitHub功能设置。

