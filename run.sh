#!/bin/bash

echo "正在启动AI女友聊天机器人..."
echo ""

# 检查是否安装了依赖
if [ ! -d "venv" ]; then
    echo "正在创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "正在安装依赖包..."
pip install -r requirements.txt

# 检查.env文件
if [ ! -f ".env" ]; then
    echo "警告: 未找到.env文件，请复制env.example并配置"
    echo "正在复制env.example到.env..."
    cp env.example .env
    echo "请编辑.env文件，设置AI_PROVIDER（推荐使用ollama）"
fi

# 启动应用
echo ""
echo "启动服务器..."
echo "访问地址: http://localhost:8000"
echo ""
python main.py

