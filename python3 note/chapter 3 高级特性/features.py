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

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	