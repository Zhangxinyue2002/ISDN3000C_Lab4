import socket
import threading
import os
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
import random

# 加载环境变量
load_dotenv()

# 配置服务器信息
HOST = '0.0.0.0'  # 监听所有可用的网络接口
PORT = 9999       # 网关服务的端口

# 创建 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),  # 使用环境变量中的 API 密钥
    base_url="https://api.chatanywhere.tech/v1"  # DeepSeek API 基础 URL
)

def chat_with_bot(user_message):
    """通过 DeepSeek API 与聊天机器人交互"""
    try:
        # 修改请求内容以增加输出的简洁性
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Please respond with 3-4 concise sentences."},
                {"role": "user", "content": user_message}
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"发生错误: {str(e)}"

def format_with_ponysay(message):
    """使用 ponysay 格式化消息"""
    command = f'echo "{message}" | ponysay'
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout.strip()

def format_with_pokemonsay(message):
    """使用 pokemonsay 格式化消息"""
    command = f'echo "{message}" | pokemonsay'
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout.strip()

def handle_client(conn, addr):
    """处理客户端的连接"""
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            request = conn.recv(1024).decode('utf-8', errors='replace')  # 使用 errors='replace' 来处理解码
            if not request:
                break

            print(f"Received request from {addr}: {request}")

            # 通过 DeepSeek API 生成回应
            ai_response = chat_with_bot(request)

            # 随机选择使用 ponysay 或 pokemonsay
            if random.choice([True, False]):
                formatted_response = format_with_ponysay(ai_response)
            else:
                formatted_response = format_with_pokemonsay(ai_response)

            # 检查返回是否是有效的 UTF-8 字符串
            try:
                utf8_response = formatted_response.encode('utf-8')
                conn.sendall(utf8_response)
            except Exception as e:
                print(f"发送响应时发生错误: {str(e)}")
                error_message = "发生错误，无法获取响应。"
                conn.sendall(error_message.encode('utf-8'))

    print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start_server():
    """启动主服务器循环以监听传入连接"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = server_socket.accept()
        # 创建新线程处理客户端连接
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()