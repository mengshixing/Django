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
    print('17:27')
	
now1()



























