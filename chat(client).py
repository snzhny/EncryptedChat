from http import client
from random import randint, random
from threading import Thread
from tracemalloc import stop
from encrypting import *
import socket


def send_message():
    while True:
        message = input("me > ")
        if '!file' in message:
            encrypted_file = encryptFile(message[6:], key)
            i = 0
            for i in range(len(encrypted_file) // 1024):
                client_socket.send(encrypted_file[i*1024:(i+1)*1024]) # отправляет файл чистично(по 1024 кБ)
            client_socket.send(encrypted_file[-1024:] + 'file!StOp!'.encode('utf-8')) 
        else:
            encrypted_text = encryptText(message, key)
            print(encrypted_text)
            i = 0
            for i in range(len(encrypted_text) // 1024):                
                client_socket.send(encrypted_text[i*1024:(i+1)*1024]) # отправляет файл чистично(по 1024 кБ)
            client_socket.send(encrypted_text[-1024:] + 'text!StOp!'.encode('utf-8')) 

            
            
            # client_socket.send('text'.encode('utf-8')) # указывает на то, что будет отправлен text
            # client_socket.send(encryptText(message, key) + '!StOp!text'.encode('utf-8'))  # encrypting.intoBase64(message[5:]).encode('utf-8'))



def receive_message():
    while True:
        data = ''
        while '!StOp!' != data[-6:]: # пока не найдет стоп-слово будет принимать данные
            data += client_socket.recv(1024).decode('utf-8')
        stop_symb_name = data.find('`!~!`') # стоп для отделения имени
        name = data[:stop_symb_name]
        data = data[stop_symb_name:] # удаление имени из строки
        data = data.replace('`!~!`', '') # удаление стоп-символа
        type = data[-10:-6] # тип данных
        data = data[:-10]
        # print(data)
        if type == 'file':
            print(f"{name} > {decryptFile(data.encode('utf-8'), key)}")
        else:
            print(f"{name} > {decryptText(data.encode('utf-8'), key)}")



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
