"""
服务器启动检查脚本
"""
import sys
import socket
import requests
import time

def check_port(host, port):
    """检查端口是否可用"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def check_server():
    """检查服务器状态"""
    print("=" * 50)
    print("🔍 检查服务器状态...")
    print("=" * 50)
    
    # 检查端口
    if check_port("127.0.0.1", 8000):
        print("✅ 端口 8000 已被占用（服务器可能正在运行）")
        
        # 尝试访问健康检查端点
        try:
            response = requests.get("http://localhost:8000/health", timeout=2)
            if response.status_code == 200:
                print("✅ 服务器运行正常！")
                print(f"📍 访问地址: http://localhost:8000")
                return True
            else:
                print(f"⚠️  服务器响应异常: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"⚠️  无法连接到服务器: {str(e)}")
            print("   可能服务器正在启动中，请稍候...")
    else:
        print("❌ 端口 8000 未被占用（服务器未运行）")
        print("   请先运行: python main.py")
    
    print("=" * 50)
    return False

if __name__ == "__main__":
    check_server()

