import socket
import threading
import os



def send_messages(client_socket, client_name):

    while True:
        message = input()
        client_socket.send(message.encode())
        file_name.writelines(message)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12348)
client_socket.connect(server_address)

name = input("Enter your name: ")
client_socket.send(name.encode())
file_name=open(name,'w')


recv_thread = threading.Thread(target=send_messages, args=(client_socket, name))
recv_thread.start()

while True:
    message = client_socket.recv(1024).decode()
    file_name.writelines(message)
    print(message)
