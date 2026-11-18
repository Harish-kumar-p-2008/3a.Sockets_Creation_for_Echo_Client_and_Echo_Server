import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5000

client_socket.connect((host, port))

while True:
    message = input("Enter Message: ")

    client_socket.sendall(message.encode())

    if message.lower() == 'exit':
        break

    data = client_socket.recv(1024).decode()

    print("Server Echoed:", data)

client_socket.close()