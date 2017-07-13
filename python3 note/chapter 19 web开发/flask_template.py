#web框架flask  pip install flask 安装 render_template

from flask import Flask,request,render_template

#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，

#print(__name__)#__main__

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
    
@app.route('/signin',methods=['get'])
def sign_form():
    return render_template('form.html')    
        
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='test' and request.form['pw']=='1':
        return render_template('sign-ok.html',username=request.form['username'])

    return render_template('form.html',
    username=request.form['username'],message='uname or pw error')

    
if __name__=='__main__':
    app.run()
    
# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，
# 还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
# 比如循环输出页码：
# {% for i in page_list %}
    # <a href="/page/{{ i }}">{{ i }}</a>
# {% endfor %}

# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。