from threading import Thread
from encrypting import *
import socket
from os import system


def send_message():
    global history
    global filePath

    filePath = str(input("Where to save all coming files(path)?: "))

    print('me > ', end='')
    while True:
        message = input()
        history += 'me > ' + message + '\n'

        if '!file' in message:
            num = message.rfind('\\')+1
            fileType = message[num:]

            encrypted_file = encryptFile(message[6:], key)
            for i in range(len(encrypted_file) // 1024):
                client_socket.send(encrypted_file[i * 1024:(i + 1) * 1024])  # partially sends a file(1024 kb)
            client_socket.send(encrypted_file[ -(len(encrypted_file) % 1024):] + ' _ '.encode() + fileType.encode('utf-8') + 'file!StOp!'.encode('utf-8'))
        else:
            encrypted_text = encryptText(message, key)
            for i in range(len(encrypted_text) // 1024):
                client_socket.send(encrypted_text[i * 1024:(i + 1) * 1024])  # partially sends a text(1024 kb)
            client_socket.send(encrypted_text[ -(len(encrypted_text) % 1024):] + 'text!StOp!'.encode('utf-8'))
        system('cls')
        print(history)
        print('me > ', end='')


def receive_message():
    global history
    while True:
        data = ''
        fileType = ''
        while '!StOp!' != data[-6:]:  # until it finds a stop word it will accept data
            data += client_socket.recv(1024).decode('utf-8')
        fileType=data[data.find(' _ ')+3:-10]
        stop_symb_name = data.find('!~!')  # stop to separate name
        name = data[:stop_symb_name]
        data = data[stop_symb_name:]  # removing a name from a string
        data = data.replace('!~!', '')  # remove stop-symbol
        dataType = data[-10:-6]
        data = data[:data.find(' _ ')]

        if dataType == 'file':
            history += f"{name} > {decryptFile(data.encode('utf-8'), key, filePath, fileType)}" + '\n'
        else:
            history += f"{name} > {decryptText(data.encode('utf-8'), key)}" + '\n'
        system('cls')
        print("Chat started...")
        print(f"{history}me > ", end='')


history = ''
if __name__ == '__main__':
    name = input('Enter your name: ')
    server_host = input('Enter ip of server: ').strip()
    server_port = 8080

    client_socket = socket.socket()
    client_socket.connect((server_host, server_port))
    client_socket.send(name.encode('utf-8'))

    g, p = (int(x) for x in (client_socket.recv(1024).decode('utf-8')).split())
    a = randint(1000, 1000000)
    ga = pow(g, a, p)
    client_socket.send(str(ga).encode())
    gb = int((client_socket.recv(1024)).decode())
    key = pow(gb, a, p)  # private key

    Thread(target=send_message).start()
    Thread(target=receive_message).start()