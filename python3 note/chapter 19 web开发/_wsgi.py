
#WSGI web server gateway interface 

#WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。

def apply(environ,start_respon):
	start_respon('200 OK',[('Content-type','text/html')])
	
	print(environ['PATH_INFO']);#/wqwqw/2121
	#environ['PATH_INFO'][1:]从第一个/去掉之后的部分
	body='<h1>hi %s ! </h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]
	
# 符合WSGI标准的一个HTTP处理函数，它接收两个参数：
    # environ：一个包含所有HTTP请求信息的dict对象；
    # start_response：一个发送HTTP响应的函数。
	# HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。
	# start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，
	# 每个Header用一个包含两个str的tuple表示。
	
# # Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现

# from wsgiref.simple_server import make_server

# from _wsgi import apply
# # 创建一个服务器，IP地址为空，端口是8000，处理函数是apply:
# httpd=make_server('',8000,apply)

# print('Serving HTTP on port 8000...')

# # 开始监听HTTP请求:

# httpd.serve_forever()


# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
# HTTP请求的所有输入信息都可以通过environ获得，
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

