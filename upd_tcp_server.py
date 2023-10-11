#!/usr/bin/env python3

import socket
import threading
import time

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print('UDP server started')

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f'Received message: {data.decode()} from {address}')

        response = 'Hello, client!'
        server_socket.sendto(response.encode(), address)

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 12345)
    message = 'Hello, server!'

    client_socket.sendto(message.encode(), server_address)

    data, address = client_socket.recvfrom(1024)
    print(f'Received response: {data.decode()} from {address}')

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

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    data = client_socket.recv(1024)
    print(f'Received message: {data.decode()} from server')

    message = 'Hello, server!'
    client_socket.send(message.encode())

    client_socket.close()

def main():
    # Create threads for UDP server and client
    udp_server_thread = threading.Thread(target=udp_server)
    udp_client_thread = threading.Thread(target=udp_client)

    # Create threads for TCP server and client
    tcp_server_thread = threading.Thread(target=tcp_server)
    tcp_client_thread = threading.Thread(target=tcp_client)

    # Start the threads
    udp_server_thread.start()
    udp_client_thread.start()
    tcp_server_thread.start()
    tcp_client_thread.start()

    # Wait for the threads to finish
    udp_server_thread.join()
    udp_client_thread.join()
    tcp_server_thread.join()
    tcp_client_thread.join()

if __name__ == '__main__':
    main()