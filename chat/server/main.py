import socket
import threading

clients = []
client_names = {}  # Store client names


def handle_client(client_socket, client_address):
    try:
        # Get client's chosen name
        name = client_socket.recv(1024).decode()
        client_names[client_socket] = name
        print(f"{name} connected from {client_address}")

        # Broadcast client's messages
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"{name}: {message}")
            for client in clients:
                if client != client_socket:
                    client.send(f"{name}: {message}".encode())
    except:
        print(f"{name} disconnected")
        clients.remove(client_socket)
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12348)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server is listening...")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    client_name_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_name_thread.start()
