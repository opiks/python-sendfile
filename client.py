import socket

def send_file(file_name, host='127.0.0.1', port=5001):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    with open(file_name, 'rb') as f:
        client_socket.send(file_name.encode())
        print(f"Sending file: {file_name}")

        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)
    
    print(f"File {file_name} sent successfully")
    client_socket.close()

if __name__ == "__main__":
    file_name = 'test.txt' 
    send_file(file_name)