import socket
from random import randint
from threading import Thread
import keyboard

def quit1():
    if not keyboard.wait('Esc'):
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
            while '!StOp!'.encode('utf-8') != data[-6:]:  # until it finds a stop word it will accept data
                data += user.recv(1024)
                count += 1
        except ConnectionResetError:
            print(f"{names[user].decode()} vishel")
            users.remove(user)
            del names[user]
            break
        str = names[user] + '!~!'.encode('utf-8') + data  # stopword that separates the name from the data
        for use in users:
            if use != user:
                for i in range(count + 1):
                    use.send(str[i * 1024:(i + 1) * 1024])  # partially sends a file(1024 kb)
        # mailing to all users except sender

def start_server():
    # first user connection
    user_socket, address = sock.accept()
    names[user_socket] = user_socket.recv(256)  # user name
    print(f"User <{names[user_socket].decode()}> connected")
    user_socket.send(f"{g} {p}".encode())
    user_ga = user_socket.recv(1024)
    users.append(user_socket)  # user ip

    while flag:
        if len(names) < numberOfConnections:
            user_socket, address = sock.accept()
            names[user_socket] = user_socket.recv(256)
            print(f"User <{names[user_socket].decode()}> connected")
            user_socket.send(f"{g} {p}".encode())
            user_gb = user_socket.recv(1024)
            user_socket.send(user_ga)

            if len(names) == 2:  # second user
                users[0].send(user_gb)
                Thread(target=resend, args=(users[0],)).start()

            users.append(user_socket)
            Thread(target=resend, args=(user_socket,)).start()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8080
    server_host = "192.168.1.6"
    print(f"IP of the server : {server_host}")
    Thread(target=quit1).start()
    numberOfConnections = 3
    sock.bind((server_host, port))
    g = randint(1000, 1000000)  # for keys
    p = randint(1000, 1000000)
    sock.listen(numberOfConnections)
    users = []
    names = {}  # usernames of clients
    flag = True
    start_server()
