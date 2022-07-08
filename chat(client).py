'''
могёт отправлять на сервер зашифрованные данные и имеет право на имя
'''

from threading import Thread
from keyboard import is_pressed as pressed
# import encrypting
import socket


def send_message():
    while True:
        message = input("me > ")
        if '!file' in message:
            client_socket.send(message.encode('utf-8'))#encrypting.intoBase64(message[5:]).encode('utf-8'))
        else:
            client_socket.send(message.encode('utf-8'))


def receive_message():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(data)


if __name__ == '__main__':
    g = 5
    n = 5
    a = 4
    ga = g ** a % n
    key =1
    name = input('Enter your name: ')
    server_host = input('Enter ip of server: ')
    server_port = 8080

    client_socket = socket.socket()
    client_socket.connect((server_host, server_port))
    client_socket.send(name.encode('utf-8'))
    Thread(target=send_message).start()
    Thread(target=receive_message).start()