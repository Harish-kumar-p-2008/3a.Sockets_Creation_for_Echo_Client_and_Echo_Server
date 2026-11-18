import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5000

server_socket.bind((host, port))
server_socket.listen(1)

print("Echo server is waiting for connection ....")

client_socket, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    data = client_socket.recv(1024).decode()

    if not data:
        print("Client disconnected.")
        break

    print("Client:", data)

    if data.lower() == "exit":
        print("Client disconnected.")
        break

    client_socket.sendall(data.encode())

client_socket.close()
server_socket.close()