# 部署指南

## 推送到GitHub

### 1. 在GitHub上创建新仓库

1. 登录GitHub
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库信息：
   - Repository name: `ai-girlfriend-chatbot` (或你喜欢的名称)
   - Description: `一个基于FastAPI的AI女友聊天机器人，支持多种AI服务提供商`
   - 选择 Public 或 Private
   - **不要**勾选 "Initialize this repository with a README"
4. 点击 "Create repository"

### 2. 连接本地仓库到GitHub

在项目目录下执行以下命令（替换 `YOUR_USERNAME` 和 `YOUR_REPO_NAME`）：

```bash
# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 或者使用SSH（如果你配置了SSH密钥）
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
```

### 3. 提交代码

```bash
# 添加所有文件
git add .

# 创建提交
git commit -m "Initial commit: AI女友聊天机器人"

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 4. 后续更新

```bash
# 添加更改
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到GitHub
git push
```

## 使用GitHub Actions进行CI/CD

项目已配置GitHub Actions工作流，在推送代码时会自动运行：
- Python代码检查
- 依赖安装测试
- 代码风格检查

## 发布到PyPI（可选）

如果你想将项目发布到PyPI：

1. 安装构建工具：
```bash
pip install build twine
```

2. 构建包：
```bash
python -m build
```

3. 上传到PyPI：
```bash
twine upload dist/*
```

## 部署到服务器

### 使用Docker（推荐）

1. 创建 `Dockerfile`：
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

2. 构建和运行：
```bash
docker build -t ai-chatbot .
docker run -p 8000:8000 ai-chatbot
```

### 使用systemd（Linux）

创建服务文件 `/etc/systemd/system/ai-chatbot.service`：

```ini
[Unit]
Description=AI Girlfriend Chatbot
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/chatbot
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

启动服务：
```bash
sudo systemctl enable ai-chatbot
sudo systemctl start ai-chatbot
```

## 环境变量配置

在服务器上创建 `.env` 文件：

```bash
cp env.example .env
nano .env  # 编辑环境变量
```

确保不要将 `.env` 文件提交到Git仓库（已在.gitignore中排除）。

## 安全建议

1. **不要提交敏感信息**：API密钥、密码等应存储在 `.env` 文件中
2. **使用HTTPS**：在生产环境使用HTTPS而不是HTTP
3. **限制访问**：使用防火墙限制端口访问
4. **定期更新**：保持依赖包的最新版本

## 故障排除

如果遇到问题，请查看：
- `TROUBLESHOOTING.md` - 故障排除指南
- GitHub Issues - 查看是否有类似问题
- 项目文档 - 查看详细说明

