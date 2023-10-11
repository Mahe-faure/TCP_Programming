#!/usr/bin/env python3

import socket
import threading

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 12345)
    message = 'Hello, server!'

    client_socket.sendto(message.encode(), server_address)

    data, address = client_socket.recvfrom(1024)
    print(f'Received response: {data.decode()} from {address}')


if __name__ == '__main__':
    udp_client_thread = threading.Thread(target=udp_client)
    udp_client_thread.start()
    udp_client_thread.join()