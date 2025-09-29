import socket
import threading
import subprocess
import random

HOST = '0.0.0.0'  # 监听所有可用的网络接口
PORT = 9999       # 网关服务的端口

def handle_client(conn, addr):
    """
    处理客户端连接的函数
    """
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            # 等待客户端请求
            request = conn.recv(1024).decode('utf-8')
            if not request:
                # 如果客户端关闭连接，退出循环
                break

            print(f"Received request from {addr}: {request}")

            # 随机选择用 Fortune 结合 Pokemonsay 或 Ponysay
            if random.choice([True, False]):
                command = ['fortune', '|', 'ponysay']
            else:
                command = ['fortune', '|', 'pokemonsay']

            # 执行命令
            fortune_response = subprocess.run(' '.join(command), shell=True, capture_output=True, text=True)

            # 检查命令执行是否成功
            if fortune_response.returncode == 0 and fortune_response.stdout:
                conn.sendall(fortune_response.stdout.encode('utf-8'))
            else:
                error_message = "Error generating response."
                conn.sendall(error_message.encode('utf-8'))

    print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start_server():
    """
    启动主服务器循环以监听传入连接
    """
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
