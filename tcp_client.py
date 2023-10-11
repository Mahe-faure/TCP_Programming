#!/usr/bin/env python3

import socket
import threading

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    data = client_socket.recv(1024)
    print(f'Received message: {data.decode()} from server')

    message = 'Hello, server!'
    client_socket.send(message.encode())

    client_socket.close()

if __name__ == '__main__':
    tcp_client_thread = threading.Thread(target=tcp_client)
    tcp_client_thread.start()
    tcp_client_thread.join()