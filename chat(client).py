'''
могёт отправлять на сервер зашифрованные данные и имеет право на имя
'''
from random import randint, random
from threading import Thread
from keyboard import is_pressed as pressed
# import encrypting
import socket


def send_message():
    while True:
        message = input("me > ")
        if '!file' in message:
            client_socket.send(message.encode('utf-8'))  # encrypting.intoBase64(message[5:]).encode('utf-8'))

        else:
            client_socket.send(message.encode('utf-8'))


def receive_message():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(data)


def receive_public_keys():
    pass


if __name__ == '__main__':
    name = input('Enter your name: ')
    server_host = input('Enter ip of server: ').strip()
    server_port = 8080

    client_socket = socket.socket()
    client_socket.connect((server_host, server_port))
    g, p = (int(x) for x in (client_socket.recv(1024).decode('utf-8')).split())
    a = randint(1, 10)
    ga = (g ** a) % p  # наш остаток
    client_socket.send(str(ga).encode())

    gb = int((client_socket.recv(1024)).decode())  # получение чужого остатка

    key = gb ** a % p
    print(f"key: {key}")
    print(g, p)
    print(a)
    print(ga)
    client_socket.send(name.encode('utf-8'))
    Thread(target=send_message).start()
    Thread(target=receive_message).start()
