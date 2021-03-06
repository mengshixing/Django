﻿#Higher-order function 高阶函数

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

#reduce函数等于函数执行后的值作为下一层嵌套的值

#reduce(f,[1,2,3,4])=f(f(f(1,2),3),4)

def f2(x,y):

    return x+y

from functools import reduce
    
print(reduce(f2,range(1,6)))

#字符串转换为整数

def f3(x,y):

    return x*10+y
    
def char2num(s):

    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    
print(reduce(f3,map(char2num,'12345')))

#优化成一个函数

def str2int(s):
    
    def f4(x,y):

        return x*10+y
        
    def char2num(s):

        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        
    return reduce(f4,map(char2num,s))
    
print(str2int('1234589'))

#使用lambda函数进一步优化(匿名函数)
        
def str2int(s):
    
    return reduce(lambda x,y:x*10+y,map(char2num,s))
    
print(str2int('87892'))

#练习1,输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

list1=['adam', 'LISA', 'barT']

print(list(map(lambda x:x.title(),list1)))

#练习2,请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(l):

    return reduce(lambda x,y:x*y,l)

print(prod(range(1,6)))

#练习3,利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):

    return reduce(lambda x,y:x*10+y,map(char2num,s.split('.')[0]+s.split('.')[1]))*(10**-len(s.split('.')[1]))

print(str2float('123.456'))

#filter函数用于过滤数列,返回函数值为true的值

print(list(filter(lambda x : x%2 ==1,range(1,11))))

#埃氏筛法取素数

def _odd_iter():

    n=1
    
    while True:
    
        n=n+2
    
        yield n
        
def _not_divisible(n):

    return lambda x: x%n >0
    
def prims():

    yield 2
    
    l=_odd_iter()
    
    while True:
    
        n=next(l)
        
        yield n
        
        l=filter(_not_divisible(n),l)
        
for n in prims():

    if n<100:
    
        print(n)
    
    else:
    
        break
        
#练习:回数是指从左向右读和从右向左读都是一样的数，例如12321。请利用filter()滤掉非回数：

print(list(filter(lambda x : str(x)[::-1]==str(x),range(1,1000))))

print(str(12345)[::-1])

#sorted()对数组排序

l3=[36, 5, -12, 9, -21]

print(sorted(l3))   

#sorted是一个高阶函数可以接受一个key参数(函数),第三个参数reverse=True反响拍序   

print(sorted(l3,key=abs))   

l4=['bob', 'about', 'Zoo', 'Credit'];

print(sorted(l4))   

print(sorted(l4,key=str.lower))   

print(sorted(l3,key=abs,reverse=True))   

#练习按名字排序

Lt = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(Lt))   

print(sorted(Lt,key= lambda x :x[1]))  





