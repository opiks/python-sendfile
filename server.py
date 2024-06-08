import socket
import os

def start_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        with conn:
            # Menerima nama file asli dari client
            original_file_name = conn.recv(1024).decode()
            if not original_file_name:
                break
            print(f"Receiving file: {original_file_name}")

            # Generate nama file baru
            new_file_name = f"received_{original_file_name}"
            with open(new_file_name, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"File received and saved as: {new_file_name}")
            exit()
if __name__ == "__main__":
    start_server()