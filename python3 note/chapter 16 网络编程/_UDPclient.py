#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('192.168.0.124', 2047))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()


# wait
# ('192.168.0.115', 44016)
# ('192.168.0.115', 44016)
# ('192.168.0.115', 44016)
