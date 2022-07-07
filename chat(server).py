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
    sock = socket.socket()
    port = 8080
    server_host = socket.gethostname()

    server_ip = socket.gethostbyname(server_host)
    print(server_ip)
    numberOfConnections = 2

    sock.bind((server_host, port))

    client_name = input("Enter your name: ")
    sock.listen(numberOfConnections)

    conn, address = sock.accept()

    client = (conn.recv(1024)).decode()
    print(f"{address[0]}({client}) has joined...")
    conn.send(client_name.encode())

    while True:
        message = input("Me > ")
        conn.send(message.encode())  # we need to create a custom encode func
        message = conn.recv(1024)  # message size: 1Kb
        message = message.decode()  # we need to create a custom decode func

        print(f"{client} > {message}")
