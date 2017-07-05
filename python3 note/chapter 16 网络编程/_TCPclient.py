#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#tcp client
import socket

#创建ipv4,tcp的socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.0.213',2046))

print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()