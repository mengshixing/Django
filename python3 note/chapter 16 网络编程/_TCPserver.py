#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#一个Socket依赖4项：服务器地址、服务器端口、客户端地址、
#客户端端口来唯一确定一个Socket。但是服务器还需要同时响应多个客户端的请求，
#所以，每个连接都需要一个新的进程或者新的线程来处理

import socket
import threading
import time
import sys
#创建ipv4,tcp的socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('',2046))

s.listen(5)
#这是说能等待连接的最大数量，通常设为5就足够了，如果服务器太忙，可以设大点

print('wait connect ...')

def tcplink(sock,addr):
    print('new connect from %s %s' % addr)
    sock.send(b'welcome')
    
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        
        if not data or data.decode('utf-8')=='exit':
            break
        #: a bytes-like object is required, not 'str'
        sock.send(('hello %s' % data.decode('utf-8')).encode('utf-8'))
    
    sock.close() 
    print('connect close %s %s' % addr)


while True:
    sock,addr=s.accept()
    #print(sock)
    #try:
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
    #finally:
        #sys.exit() 
