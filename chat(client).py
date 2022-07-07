#!/usr/bin/python3
"""
Client-side chat
"""
try:
    import socket
    import sys
    import tor
    import time
except ModuleNotFoundError:
    from subprocess import call
    modules = ["tor"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    server_socket = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    server_port = 8080

    server_host = input('Enter ip of server: ')
    name = input('Enter your name: ')

    server_socket.connect((server_host, server_port))

    server_socket.send(name.encode())
    server_name = server_socket.recv(1024)
    server_name = server_name.decode()

    print("You joined")

    while True:
        message = (server_socket.recv(1024)).decode()
        print(server_name, ">", message)
        message = input("Me > ")
        server_socket.send(message.encode())