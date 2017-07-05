#创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。
#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
#而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可

import socket
#创建一个socket
#socket.AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
#SOCK_STREAM指定使用面向流的TCP协议

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立链接
#例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，
#端口号大于1024的，可以任意使用。
s.connect(('www.sina.com.cn',80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，
# 怎么协调，要根据具体的协议来决定。例如，HTTP协议规定客户端
# 必须先发请求给服务器，服务器收到后才发数据给客户端。

buffer=[]
while True:
    #每次最多接受1K
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
        
data=b''.join(buffer)
s.close()#关闭

header,html=data.split(b'\r\n\r\n',1)#找到第一个分隔符,分成2部分
print(header.decode('utf-8'))

# HTTP/1.1 200 OK
# Server: nginx
# Date: Wed, 05 Jul 2017 03:03:54 GMT
# Content-Type: text/html
# Last-Modified: Wed, 05 Jul 2017 03:01:51 GMT
# Vary: Accept-Encoding
# Expires: Wed, 05 Jul 2017 03:04:54 GMT
# Cache-Control: max-age=60
# X-Powered-By: shci_v1.03
# Content-Length: 595854
# X-Cache: HIT from cnc.tianjin.sinacache.92.nb.sinaedge.com
# Connection: close


with open('sina.html','wb') as f:
    f.write(html)
        
# with open('sina1.html','wb',encoding='utf-8',errors='ignore') as f:
    # f.write(html)
# ValueError: binary mode doesn't take an encoding argument
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

