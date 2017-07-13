#web框架flask  pip install flask 安装 

from flask import Flask
from flask import request

#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，

#print(__name__)#__main__

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
    
@app.route('/signin',methods=['get'])
def sign_form():
    return "<form action='/signin' method='post'>\
        <p><input name='username'></p>\
        <p><input name='pw'></p>\
        <p><button type='submit'>Signin</button></p>"
        
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='test' and request.form['pw']=='1':
        return '<h2>login success<h2>'
    return '<h2>login failed<h2>'
	
if __name__=='__main__':
	app.run()
	
 # * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 127.0.0.1 - - [13/Jul/2017 14:55:25] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [13/Jul/2017 14:55:36] "GET /signin HTTP/1.1" 200 -
# 127.0.0.1 - - [13/Jul/2017 14:55:43] "POST /signin HTTP/1.1" 200 -