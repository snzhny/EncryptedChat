'''
сервер принимает в себя отправлялки от клиента и отправляет их всем другим клиeнтам
'''

import socket
from random import randint
from subprocess import call
from threading import Thread

import keyboard


def quit1():
    if not keyboard.wait('Esc'):
        print(5675454)
        flag = False
        # sock.shutdown(socket.SHUT_RDWR)
        for userik in users:
            Thread(target=resend, args=(userik,)).join()
        quit()
        call("exit")

def resend(user):
    while flag:
        data = user.recv(1024)
        for use in users:
            if use != user:
                use.send(names[user] + " > ".encode('utf-8') + data)  # отправляет всем юзерам, кроме того кто это отправил


def start_server():
    while flag:
        user_socket, address = sock.accept()
        print(f"User <{address[0]}> connected")
        user_socket.send(f"{g} {p}".encode())
        names[user_socket] = user_socket.recv(256)  # имя пользователя
        users.append(user_socket)  # ip пользователя
        Thread(target=resend, args=(user_socket,)).start()


if __name__ == '__main__':
    sock = socket.socket()
    port = 8080
    server_host = "192.168.0.82"  # socket.gethostname()
    # server_host = socket.gethostname()
    server_ip = socket.gethostbyname(server_host)
    print(f"IP of the server : {server_ip}")
    Thread(target=quit1).start()
    numberOfConnections = 2
    sock.bind((server_host, port))
    g = randint(1, 10)
    p = randint(1, 10)
    print(g, p)
    sock.listen(numberOfConnections)
    users = []
    names = {}  # usernames of clients
    flag = True
    start_server()
