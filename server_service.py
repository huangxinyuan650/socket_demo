# -*- coding: utf-8 -*-
"""
    @author:hxy
    @file:service.py
    @time:2019-08-22
"""

import socket
import threading
import logging


def receive_msg_thread(addr, client):
    while True:
        msg = client.recv(1024)
        print('Message from {}:{}\n'.format(addr, msg.decode('utf-8')))


def send_msg_thread(addr, server):
    while True:
        msg_str = input()
        print('Message send to {}:{}'.format(addr, msg_str))
        server.send(msg_str.encode('utf-8'))


def start_app(server_ip='127.0.0.1', port=6650):
    """
    服务端监听指定端口
    :param server_ip:
    :param port:
    :return:
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen(1)
    while True:
        logging.info('Waiting connection...')
        _client, addr = server.accept()
        print('Connection from {}'.format(addr))
        receive_thread = threading.Thread(target=receive_msg_thread, args=(addr, _client))
        receive_thread.setDaemon(True)
        receive_thread.start()
        send_thread = threading.Thread(target=send_msg_thread, args=(addr, _client))
        send_thread.setDaemon(True)
        send_thread.start()


if __name__ == '__main__':
    start_app()
