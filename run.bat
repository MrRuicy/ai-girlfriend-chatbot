@echo off
echo 正在启动AI女友聊天机器人...
echo.

REM 检查是否安装了依赖
if not exist "venv\" (
    echo 正在创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 安装依赖
echo 正在安装依赖包...
pip install -r requirements.txt

REM 检查.env文件
if not exist ".env" (
    echo 警告: 未找到.env文件，请复制env.example并配置
    echo 正在复制env.example到.env...
    copy env.example .env
    echo 请编辑.env文件，设置AI_PROVIDER（推荐使用ollama）
)

REM 启动应用
echo.
echo 启动服务器...
echo 访问地址: http://localhost:8000
echo.
python main.py

pause

