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