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

	
	
	
	
	
	
	
	
	