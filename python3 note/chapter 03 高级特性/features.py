#比如构造一个1, 3, 5, 7, ..., 99的列表

n=1;L=[]

while n<100:

    L.append(n)
    
    n=n+2
    
print(L)

#切片Slice

#切取前三个元素,索引从0开始到3,不含3 也可以直接:3

print(L[0:3]) ; print(L[:3])

#切取2到4元素,索引从1开始到4,不含4

print(L[1:4]) 

#倒数切片 倒数切片第一个元素是-1

print(L[-2:]) 

#前十每2个取一个

print(L[:10:2]) 

#只写:切全部 ,所以的元素每5个切一下

print(L[::5]) 

#tuple和字符串也可以切片

print((1,2,3,4,5)[::2])

print('1,2,3,4,5'[:5])

#迭代Iteration 通过for..in来实现,可以迭代list,tuple,dict,字符串等

D={'a':1,'b':2,'c':222}

for key in D:
        print(key)
    
for value in D.values():
    
    print(value)

for k,v in D.items():
    
    print(k,v)
    
#通过collections模块的iterable类型来判断

from collections import Iterable
    
print(isinstance('ABC',Iterable))

print(isinstance(124,Iterable))

#enumerate函数能把list变成键值对

for k,v in enumerate(L[:4]):

    print(k,v)
    
#还有就是for循环能有多个参数

for a,b,c in [(1,2,3),(3,4,5),(7,8,9)]:

    print(a,b,c)

#列表生成式List Comprehensions,用于创建list

print(list(range(1,10)))
    
print([x*x for x in range(1,11)])
    
print([x*x for x in range(1,11) if x%3==0]) 
    
print([a+b+c for a in 'ABC' for b in 'def' for c in 'OPQ'])     
    
#导入文件系统os列出文件夹下文件

import os

print([d for d in os.listdir('.')])
    
#列表生成式也可以使用两个变量来生成list：

d={'x':'a','y':'b'}
    
print([k+'='+v for k,v in d.items()])   

#练习list中既包含字符串，又包含整数，转换为小写

test1=[12,'Hello',{1,2,3}]
    
print([s.lower() for s in test1 if isinstance(s,str)])  

#列表生成式和生成器区别在于[]和(),第一种generator生产方法

g=(x*x for x in range(1,11))

print(next(g),next(g),next(g))

#generator保存的是算法,调用next()时生成下一个值,也可以使用for

for x in g:

    print(x)

#对于问波拉契数列

def fib(x):

    n,a,b=0,0,1
    
    while n<x:
    
        print(b)
    
        a,b=b,a+b
        
        n=n+1
        
    return 'done'
    
print(fib(10))
    
#第二种方法生成generator使用yield即可,含yield的函数即为一个generator

def fib1(x):

    n,a,b=0,0,1
    
    while n<x:
    
        yield(b)
    
        a,b=b,a+b
        
        n=n+1
        
    return 'done'
    
print(next(fib1(10)))

#获取return返回值只能通过捕获异常

sex=fib1(10)

while True:

    try:
    
        y=next(sex)
    
        print(y)
        
    except StopIteration as e:
    
        print(e.value)
        
        break
        
#练习杨辉三角

def triangle():

    qqq=[1]
    
    while True:
    
        yield(qqq)  
        
        qqq=[ x+y for x,y in zip(qqq[:-1],qqq[1:]) ]
        
        qqq.insert(0,1);qqq.append(1)
        
mmm=triangle()

i=0;

while i<10:

    print(next(mmm))
    
    i=i+1

#可以进行for循环的一类是集合list,tuple,dict,set,str,一类是generator

#统称可迭代对象Iterable,可使用isinstance()判断

from collections import Iterable

print(isinstance([],Iterable))

print(isinstance({},Iterable))

print(isinstance('aaa',Iterable))

print(isinstance(100,Iterable))

print(isinstance((x for x in range(1,10)),Iterable))

#可以使用next()获取下一个值的称为迭代器 Iterator

from collections import Iterator

print(isinstance([],Iterator))

print(isinstance({},Iterator))

print(isinstance('aaa',Iterator))

print(isinstance(100,Iterator))

print(isinstance((x for x in range(1,10)),Iterator))

#Iterator对象实际是一个数据流 iter()方法可以转换list等为Iterator

print(isinstance(iter([]),Iterator))

print(isinstance(iter({}),Iterator))

print(isinstance(iter('aaa'),Iterator))

#凡是可作用于for循环的对象都是Iterable类型,凡是可作用于next()函数的对象都是Iterator类型

for x in range(1,6):

    print(x)
    
#等价于

LMS=range(1,6)

while True:

    try:
    
        print(next(iter(LMS)))
        
    except StopIteration:
    
        break
 
    