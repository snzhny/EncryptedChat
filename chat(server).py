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
    while True:
        try:
            type = user.recv(100) # тип файла
            data = user.recv(4096) # сам файл
        except ConnectionResetError:
            print(f"chel vishel")
            break
        for use in users:
            if use != user:
                use.send(type)
                use.send(data)
                use.send(names[user]) # имя клиента
           # отправляет всем юзерам, кроме того кто это отправил

def start_server():
    while flag:
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
    numberOfConnections = 2
    sock.bind((server_host, port))
    g = randint(1, 10)  # for keys
    p = randint(1, 10)  # for keys
    sock.listen(numberOfConnections)
    users = []
    names = {}  # usernames of clients
    flag = True
    start_server()
