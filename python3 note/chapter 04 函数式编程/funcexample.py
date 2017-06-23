#返回函数,高阶函数可以把函数作为返回值返回

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
    
f1=lazy_sum(*list(range(1,11)))
f3=lazy_sum(*list(range(1,11)))
f2=lazy_sum(*list(range(1,21)))
print(f1)
print(f1())
print(f2())
print(f1==f3)

#即闭包,f1,f3调用毫不影响,闭包即返回的函数还保留着函数内变量的引用

def count():
    list=[]
    for i in range(1,4):
        def f():
            return i*i
        list.append(f)
    return list
    
f4,f5,f6=count()
print(f4())
print(f5())
print(f6())
f7=count()
print(f7)

#由于闭包返回是含有循环变量,返回的数组含3个函数，引用的i都是3,可以修改如下：

def count():
    list=[]
    
    for i in range(1,4):
        def f(i):
            return lambda :i*i
        list.append(f(i))
    return list
    
f7,f8,f9=count()
print(f7())
print(f8())
print(f9())

#修改后对每个i引用返回一个闭包函数
#匿名函数lambda不需要函数名,可以作为函数返回值

f10=lambda x:x*x
print(f10(10))

def build(x,y):
    return lambda:x*x+y*y
print(build(3,4))
print(build(3,4)())

#函数对象有一个_name_属性
def now():
    print('17:27')
f11=now
f11()
print(now.__name__)

#在代码动态运行过程中添加功能的方式,称装饰器Decorator

#本质上是一个返回函数的高阶函数，打印日志

def log(func):
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now1():
    print('17:37')
    
now1()

#如果装饰器本身有参数的话

def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
    
@log2('execute')
def now2():
    print('17:47')
now2();
print(now2.__name__)

#此时now2的name被替换成了wrapper,引入functools即可

import functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
    
@log3('execute')
def now3():
    print('17:47')
now3();
print(now3.__name__)

#练习请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def log4(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call")
        func(*args,**kw)
        print("end call")
    return wrapper

@log4
def now4():
    print('17:57')
now4();
print(now4.__name__)

#练习请编写一个decorator，能在函数调用支持log传不传参。

def log5(text):
    if(isinstance(text,str)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print("%s %s():" % (text,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print("begin call")
            text(*args,**kw)
            print("end call")
        return wrapper

@log5
def now5():
    print('16:57')
now5();
print(now5.__name__)

#functools.partial可以用来创建一个偏函数
#x是2进制的 int之后统一变为10进制的整数
def int2(x,type=2):
    return int(x,type)
    
print(int2('111111111'))
print(int2('199',16))

int3=functools.partial(int,base=2)

print(int3('111111111'))
print(int3('199',base=16))

#相当于kw={'base':2} int3(x,**kw)

max2=functools.partial(max,10)

#相当与把10作为*args放到最左边

print(max2(1,23))
print(max2(1,2,3))





