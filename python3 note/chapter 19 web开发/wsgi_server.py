# Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现

from wsgiref.simple_server import make_server

from _wsgi import apply
# 创建一个服务器，IP地址为空，端口是8000，处理函数是apply:
httpd=make_server('192.168.0.115',8000,apply)

print('Serving HTTP on port 8000...')

# 开始监听HTTP请求:

httpd.serve_forever()

# 日志
# [root@localhost opt]# python wsgi_server.py 
# Serving HTTP on port 8000...
# 192.168.0.124 - - [13/Jul/2017 18:24:24] "GET / HTTP/1.1" 200 19
# 192.168.0.124 - - [13/Jul/2017 18:24:24] "GET /favicon.ico HTTP/1.1" 200 19