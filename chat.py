#!/usr/bin/python3
"""
Server-side chat
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
    port = 8080
    server_host = socket.gethostname()
    server_ip = socket.gethostbyname(server_host)
    numberOfConnections = 2

    server_socket.bind((server_host, port))

    client_name = input("Enter your name: ")
    server_socket.listen(numberOfConnections)

    conn, address = server_socket.accept()
    print(f"Received connection from: {address[0]}")

    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')
    conn.send(client_name.encode())

    while True:
        message = input("Me > ")
        conn.send(message.encode())  # we need to create a custom encode func
        message = conn.recv(1024)  # message size: 1Kb
        message = message.decode()  # we need to create a custom decode func

        print(f"{client} > {message}")
