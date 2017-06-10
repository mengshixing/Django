#Higher-order function 高阶函数

#变量可以指向函数

print(abs(-10))

f=abs

print(f(-10))

print(f)

#函数名也是变量,指向函数,由于abs函数实际上是定义在import builtins模块中的，

#所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

#abs=10

#print(abs(-10))

#一个函数接受另一个函数作为参数,称为高阶函数

def add(a,b,f):

    return f(a)+f(b)
    
print(add(2,-2,abs))

#map()和reduce()函数,map接受一个函数和一个Iterable,返回一个Iterator

def f1(x):

    return x*x
   
#Iterrator是惰性数列,所以通过list()把整个数列计算出来返回一个list
   
print(list(map(f1,range(1,6)))) 

print(list(map(str,'hello world !')))
