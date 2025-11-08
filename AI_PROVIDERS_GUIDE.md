# AI服务提供商配置指南

## 🎯 推荐方案（按优先级）

### 1. 🆓 Ollama - 完全免费本地模型（强烈推荐）

**优点：**
- ✅ 完全免费，无API费用
- ✅ 本地运行，数据隐私安全
- ✅ 无需网络连接（下载模型后）
- ✅ 中文支持优秀（qwen模型）

**安装步骤：**

1. **下载并安装Ollama**
   - 访问: https://ollama.ai
   - 下载对应系统的安装包
   - 安装后，Ollama会自动运行

2. **下载AI模型**
   ```bash
   # 推荐模型（中文优秀）
   ollama pull qwen2.5:7b
   
   # 或者使用轻量级模型（速度更快）
   ollama pull qwen2.5:1.5b
   
   # 或者使用其他模型
   ollama pull llama3.2:3b
   ollama pull mistral:7b
   ```

3. **配置.env文件**
   ```env
   AI_PROVIDER=ollama
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL_NAME=qwen2.5:7b
   ```

4. **启动应用**
   ```bash
   python main.py
   ```

**推荐模型：**
- `qwen2.5:7b` - 中文支持最好，推荐用于中文对话
- `qwen2.5:1.5b` - 轻量级，速度快，适合低配置电脑
- `llama3.2:3b` - 通用模型，速度快
- `mistral:7b` - 英文优秀

---

### 2. 💰 OpenAI API - 需要付费

**优点：**
- ✅ 回复质量高
- ✅ 响应速度快
- ✅ 稳定可靠

**缺点：**
- ❌ 需要API密钥
- ❌ 需要付费（按使用量计费）

**配置步骤：**

1. **获取API密钥**
   - 访问: https://platform.openai.com
   - 注册账号并获取API密钥

2. **配置.env文件**
   ```env
   AI_PROVIDER=openai
   OPENAI_API_KEY=sk-your-api-key-here
   OPENAI_MODEL_NAME=gpt-3.5-turbo
   ```

3. **安装依赖**
   ```bash
   pip install openai
   ```

---

### 3. 🆓 Google Gemini - 有免费额度

**优点：**
- ✅ 有免费额度
- ✅ 回复质量好

**缺点：**
- ❌ 需要API密钥
- ❌ 免费额度有限

**配置步骤：**

1. **获取API密钥**
   - 访问: https://makersuite.google.com/app/apikey
   - 获取API密钥

2. **配置.env文件**
   ```env
   AI_PROVIDER=gemini
   GEMINI_API_KEY=your-gemini-api-key-here
   GEMINI_MODEL_NAME=gemini-pro
   ```

3. **安装依赖**
   ```bash
   pip install google-generativeai
   ```

---

### 4. 💰 Anthropic Claude - 需要付费

**优点：**
- ✅ 回复质量优秀
- ✅ 安全性好

**缺点：**
- ❌ 需要API密钥
- ❌ 需要付费

**配置步骤：**

1. **获取API密钥**
   - 访问: https://console.anthropic.com
   - 注册账号并获取API密钥

2. **配置.env文件**
   ```env
   AI_PROVIDER=claude
   CLAUDE_API_KEY=your-claude-api-key-here
   CLAUDE_MODEL_NAME=claude-3-haiku-20240307
   ```

3. **安装依赖**
   ```bash
   pip install anthropic
   ```

---

## 📊 对比表

| 服务提供商 | 费用 | 中文支持 | 速度 | 隐私 | 推荐度 |
|----------|------|---------|------|------|--------|
| Ollama | 🆓 免费 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| OpenAI | 💰 付费 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Gemini | 🆓 免费额度 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Claude | 💰 付费 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🚀 快速切换

只需修改 `.env` 文件中的 `AI_PROVIDER` 即可切换不同的AI服务：

```env
# 使用Ollama (免费)
AI_PROVIDER=ollama

# 使用OpenAI
AI_PROVIDER=openai

# 使用Gemini
AI_PROVIDER=gemini

# 使用Claude
AI_PROVIDER=claude
```

然后重启应用即可。

---

## ❓ 常见问题

### Q: Ollama模型下载很慢怎么办？
A: 可以使用国内镜像或VPN加速下载。

### Q: 我的电脑配置较低，应该使用哪个模型？
A: 推荐使用 `qwen2.5:1.5b` 或 `llama3.2:3b`，这些模型较小，运行速度快。

### Q: 如何查看Ollama已下载的模型？
A: 运行命令: `ollama list`

### Q: 可以同时使用多个AI服务吗？
A: 不可以，一次只能使用一个AI服务提供商。但可以随时切换。

### Q: Ollama需要多少内存？
A: 7B模型大约需要8GB内存，3B模型需要4GB内存，1.5B模型需要2GB内存。

---

## 💡 建议

**对于中文用户，强烈推荐使用Ollama + qwen2.5:7b模型**，这是目前最好的免费中文AI方案。

