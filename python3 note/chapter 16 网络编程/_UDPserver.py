#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('',2047))

# SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要
# 调用listen()方法，而是直接接收来自任何客户端的数据：

print('wait')

while True:
    
    data,addr=s.recvfrom(1024)
    
    print(addr)
    
    s.sendto(b' hi %s' % data,addr)
    
# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，
# 直接调用sendto()就可以把数据用UDP发给客户端。注意这里省掉了多线程，因为这个例子很简单。

 # hi Michael
 # hi Tracy
 # hi Sarah