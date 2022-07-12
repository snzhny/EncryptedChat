import socket
from random import randint
from subprocess import call
from threading import Thread
import keyboard


def quit1():
    if not keyboard.wait('Esc'):
        print(5675454)
        flag = False
        for userik in users:
            Thread(target=start_server, args=(userik,)).join()
            Thread(target=resend, args=(userik,)).join()
        sock.close()
        quit() 


def resend(user):
    while True:
        try:
            data = ''.encode('utf-8')
            count = 0
            while '!StOp!'.encode('utf-8') != data[-6:]: # пока не найдет стоп-слово будет принимать данные
                data += user.recv(1024)
                count += 1
        except ConnectionResetError:
            print(f"{names[user]} vishel")
            users.remove(user)
            del names[user]
            break
        str = names[user] + '`!~!`'.encode('utf-8') + data # стоп-слово, которое отделяет имя от данных
        for use in users:
            if use != user:
                for i in range(count+1):
                    use.send(str[i*1024:(i+1)*1024]) # отправляет файл чистично(по 1024 кБ)
           # отправляет всем юзерам, кроме того кто это отправил

def start_server():
    while flag:
        if len(names) < numberOfConnections:
            user_socket, address = sock.accept()
            print(f"User <{address[0]}> connected")
            user_socket.send(f"{g} {p}".encode())
            data_gb = user_socket.recv(1024)

            user_socket.send(data_gb)
            names[user_socket] = user_socket.recv(256)  # имя пользователя
            users.append(user_socket)  # ip пользователя
            Thread(target=resend, args=(user_socket,)).start()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8080
    server_host = "192.168.100.33"
    # server_host = socket.gethostname()
    server_ip = socket.gethostbyname(server_host)
    print(f"IP of the server : {server_ip}")
    Thread(target=quit1).start()
    numberOfConnections = 3
    sock.bind((server_host, port))
    g = randint(1, 10)  # for keys
    p = randint(1, 10)  # for keys
    sock.listen(numberOfConnections)
    users = []
    names = {}  # usernames of clients
    flag = True
    start_server()
