#!/usr/bin/env python3

import socket
import threading

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print('TCP server started')

    while True:
        client_socket, address = server_socket.accept()
        print(f'New connection from {address}')

        message = 'Hello, client!'
        client_socket.send(message.encode())

        data = client_socket.recv(1024)
        print(f'Received message: {data.decode()} from {address}')

        client_socket.close()

if __name__ == '__main__':
    tcp_server_thread = threading.Thread(target=tcp_server)
    tcp_server_thread.start()
    tcp_server_thread.join()