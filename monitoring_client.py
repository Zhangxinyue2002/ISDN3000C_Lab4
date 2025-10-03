import socket

SERVER_IP = '192.168.127.10'  # RDK-X5 的 IP 地址
SERVER_PORT = 9999

def run_client():
    while True:
        user_input = input("Is there anything I can help you? Type it here!（or type 'exit' to end）：")
        if user_input.lower() == 'exit':
            break

        try:
            # 创建 socket 并连接服务器
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((SERVER_IP, SERVER_PORT))
                client_socket.sendall(user_input.encode('utf-8'))  # 发送用户烦恼的信息
                
                # 接收服务器的响应
                response = client_socket.recv(4096)  
                response_string = response.decode('utf-8')
                
                print("RDK-X5 's feedback:")
                print(response_string)

        except ConnectionRefusedError:
            print("Connection failed. ")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_client()
