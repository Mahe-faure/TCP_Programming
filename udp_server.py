#!/usr/bin/env python3

import socket
import threading

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print('UDP server started')

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f'Received message: {data.decode()} from {address}')

        response = 'Hello, client!'
        server_socket.sendto(response.encode(), address)

if __name__ == '__main__':
    udp_server_thread = threading.Thread(target=udp_server)
    udp_server_thread.start()
    udp_server_thread.join()