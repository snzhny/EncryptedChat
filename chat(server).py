"""
сервер принимает в себя отправлялки от клиента и отправляет их всем другим клиeнтам
"""

from threading import Thread
from keyboard import is_pressed as pressed
import socket

def quit():
    while True:
        if pressed('Esc'):
            flag = False

def resend(user):
    while flag:
        data = user.recv(1024)
        print(data.decode())
        for use in users:
            if use != user:
                use.send(names)
                use.send(data)  # отправляет всем юзерам, кроме того кто это отправил

def start_server():
    while flag:
        user_socket, address = sock.accept()
        print(f"User <{address[0]}> connected")
        names.append(user_socket.recv(256))  # имя пользователя
        users.append(user_socket)  # ip пользователя
        Thread(target=resend, args=(user_socket,)).start()

if __name__ == '__main__':
    sock = socket.socket()
    port = 8080
    server_host = socket.gethostname()
    server_ip = socket.gethostbyname(server_host)
    print(f"IP of the server : {server_ip}")

    numberOfConnections = 5
    sock.bind((server_host, port))
    sock.listen(numberOfConnections)
    users = []
    names = []
    flag = True
    start_server()