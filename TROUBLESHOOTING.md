# 故障排除指南

## 502错误 - 网关错误

### 问题描述
访问网页时出现 "HTTP ERROR 502" 或 "该网页无法正常运作"。

### 解决方案

#### 1. 检查访问地址
❌ **错误**: 直接访问 `http://0.0.0.0:8000`
✅ **正确**: 访问 `http://localhost:8000` 或 `http://127.0.0.1:8000`

**原因**: `0.0.0.0` 是服务器绑定地址，不是浏览器访问地址。

#### 2. 检查服务器是否运行
运行以下命令检查服务器状态：
```bash
python check_server.py
```

或者手动检查：
```bash
# Windows
netstat -ano | findstr :8000

# Linux/Mac
lsof -i :8000
```

#### 3. 重新启动服务器
```bash
# 停止当前运行的服务器（Ctrl+C）
# 然后重新启动
python main.py
```

#### 4. 检查端口占用
如果端口8000被占用，可以：
- 关闭占用端口的程序
- 或者修改 `main.py` 中的端口号

#### 5. 检查依赖安装
确保所有依赖都已正确安装：
```bash
pip install -r requirements.txt
```

#### 6. 检查环境变量
确保 `.env` 文件存在且配置正确：
```bash
# Windows
copy env.example .env

# Linux/Mac
cp env.example .env
```

然后编辑 `.env` 文件，填入正确的API密钥。

## 其他常见问题

### OpenAI API错误
- 检查API密钥是否正确
- 检查API余额是否充足
- 检查网络连接

### 数据库错误
- 删除 `chatbot.db` 文件，重新启动服务器
- 检查文件权限

### 导入错误
- 确保虚拟环境已激活
- 重新安装依赖：`pip install -r requirements.txt`

## 获取帮助

如果问题仍未解决，请：
1. 查看服务器控制台的错误信息
2. 检查浏览器控制台的错误信息（F12）
3. 提供完整的错误日志

