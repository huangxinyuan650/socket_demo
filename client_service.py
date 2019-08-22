# -*- coding: utf-8 -*-
"""
    @author:hxy
    @file:service.py
    @time:2019-08-22
"""

import socket
import threading


def receive_msg_thread(addr, client):
    while True:
        msg = client.recv(1024)
        print('Message from {}:{}\n'.format(addr, msg.decode()))


# def send_msg_thread(addr, server):
#     while True:
#         msg_str = input('Please input message:')
#         print ('Message send to {}:{}'.format(addr, msg_str))
#         server.send('Receive')


def start_app(server_ip='127.0.0.1', port=6650):
    """
    服务端监听指定端口
    :param server_ip:
    :param port:
    :return:
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    receive_thread = threading.Thread(target=receive_msg_thread, args=(server_ip, client))
    receive_thread.setDaemon(True)
    receive_thread.start()
    while True:
        msg_str = str(input())
        print('Message send to {}:{}'.format(server_ip, msg_str))
        client.send(msg_str.encode('utf-8'))


if __name__ == '__main__':
    start_app()
