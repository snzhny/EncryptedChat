"""
могёт отправлять на сервер зашифрованные данные и имеет право на имя
"""
from random import randint, random
from threading import Thread
from keyboard import is_pressed as pressed
from encrypt_and_decrypt import *
import socket


def send_message():
    while True:
        message = input("me > ")
        if '!file' in message:
            client_socket.send(encryptFile(message[6:], key))
        else:
            client_socket.send(bytes(encryptText(message, key)))  # encrypting.intoBase64(message[5:]).encode('utf-8'))



def receive_message():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        decryptedData = decryptText(data, key)
        print(decryptedData)


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
    client_socket.send(name.encode('utf-8'))
    Thread(target=send_message).start()
    Thread(target=receive_message).start()
