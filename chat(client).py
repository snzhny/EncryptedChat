from random import randint, random
from threading import Thread
from encrypting import *
import socket


def send_message():
    while True:
        message = input("me > ")
        if '!file' in message:
            client_socket.send('file'.encode('utf-8')) # указывает на то, что будет отправлен файл
            client_socket.send(encryptFile(message[6:], key))
        else:
            client_socket.send('text'.encode('utf-8')) # указывает на то, что будет отправлен text
            client_socket.send(encryptText(message, key))  # encrypting.intoBase64(message[5:]).encode('utf-8'))



def receive_message():
    while True:
        type = client_socket.recv(100).decode('utf-8') # тип файла
        data = client_socket.recv(4096)
        name = client_socket.recv(256).decode('utf-8')
        if type == 'file':
            print(f"{name} > {decryptFile(data, key)}")
        else:
            decryptedData = decryptText(data, key)
            print(f"{name} > {decryptedData}")



if __name__ == '__main__':
    name = input('Enter your name: ')
    server_host = '192.168.100.33'#input('Enter ip of server: ').strip()
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
