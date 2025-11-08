#!/bin/bash

echo "============================================"
echo "Ollama 安装和配置脚本"
echo "============================================"
echo ""

echo "步骤1: 检查Ollama是否已安装..."
if ! command -v ollama &> /dev/null; then
    echo "Ollama未安装，请先安装Ollama"
    echo ""
    echo "安装步骤:"
    echo "1. 访问 https://ollama.ai"
    echo "2. 下载并安装Ollama"
    echo "3. 安装完成后重新运行此脚本"
    echo ""
    exit 1
fi

echo "✅ Ollama已安装"
echo ""

echo "步骤2: 检查Ollama服务是否运行..."
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "⚠️  Ollama服务未运行，正在启动..."
    ollama serve &
    sleep 3
fi

echo "✅ Ollama服务运行中"
echo ""

echo "步骤3: 查看已下载的模型..."
ollama list
echo ""

echo "步骤4: 下载推荐模型（qwen2.5:1.5b）..."
echo "这是一个轻量级模型，大小约1GB，速度快"
echo "下载可能需要一些时间，请耐心等待..."
echo ""
ollama pull qwen2.5:1.5b

echo ""
echo "============================================"
echo "配置完成！"
echo "============================================"
echo ""
echo "接下来请:"
echo "1. 确保 .env 文件中设置了:"
echo "   AI_PROVIDER=ollama"
echo "   OLLAMA_MODEL_NAME=qwen2.5:1.5b"
echo ""
echo "2. 运行: python main.py"
echo ""

