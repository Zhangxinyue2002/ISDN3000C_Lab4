import socket
import threading
import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置服务器信息
HOST = '0.0.0.0'  # 监听所有可用的网络接口
PORT = 9999       # 网关服务的端口

# 创建 OpenAI 客户端，并使用环境变量中的 API 密钥
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

def chat_with_bot(user_message):
    """通过 OpenAI API 与聊天机器人交互"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # 使用合适的模型
            messages=[
                {"role": "user", "content": user_message}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"发生错误: {str(e)}"

def handle_client(conn, addr):
    """处理客户端的连接"""
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            request = conn.recv(1024).decode('utf-8')
            if not request:
                break

            print(f"Received request from {addr}: {request}")

            # 通过聊天 API 生成回应
            ai_response = chat_with_bot(request)

            # 包装回应
            wrapped_response = f"🎉 [Chatbot Says] 🎉\n{ai_response}"
            conn.sendall(wrapped_response.encode('utf-8'))

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
