#函数 

#abs 绝对值函数

print(abs(10),abs(-100),abs(1.09e5));

#函数参数数量/类型不对的话,会报TypeError

#max()函数接收任意多参数可以

print(max(10,122,1))

#类型转换函数

print(int('1223'))

print(str(1223))

print(float(1223))

print(bool(1223))

print(bool(-1223))

print(bool(0))

a=str

print(a(2222))

#练习 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

print(hex(255))

#def 定义函数 return来返回 //return None等于return,当没有return时最后返回

#引用函数 from 文件名/不带后缀 import 函数名 空函数pass可以用来占位

def nothing():

    pass
    
#参数个数/类型 错误检测

def myfirstfuc(x,y):

    if not isinstance(x,(int,float)):
    
        raise TypeError('bad operand type')
        
    return x

#print(myfirstfuc('255a',11))

#返回多个返回值,实际上是返回了一个tuple

#练习//  请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax2 + bx + c = 0的两个解。

import math

def quadratic(a,b,c):

    if not (isinstance(a,(int)) and isinstance(b,(int)) and isinstance(c,(int))):
        
        raise TypeError('bad operand type')
        
    else:
    
        q= b*b-4*a*c
        
        if q>=0:
        
            return (-b+math.sqrt(q))/(2*a),(-b+math.sqrt(q))/(2*a)
        
        else:
            
            return None

print(quadratic(1,-2,1))
    
# 函数可以有默认参数

def qurter(x,n=2):

    sum=1;
    
    while n>0:
    
        sum=sum*x
        
        n=n-1
        
    return sum
    
print(qurter(5))    

print(qurter(5,4))

#默认函数def enroll(name, gender, age=6, city='Beijing'):  可以输入

#enroll('Bob', 'M', 7)或者enroll('Adam', 'M', city='Tianjin')

def add_end(l=[]):

    l.append(11)
    
    return l
    
print(add_end([1,2]))

print(add_end())

print(add_end())

#定义默认参数要牢记一点：默认参数必须指向不变对象！上面函数修改如下

def add_end1(l=None):

    if l is None:
    
        l=[]; 
    
    l.append(11)
    
    return l
   
print(add_end1([1,2]))

print(add_end1())

print(add_end1())

#可变参数 传入list,tuple的话类似calc(1, 2, 3),普通要传calc([1, 2, 3])

def calc(*numbers):

    sum=0
    
    for n in numbers:
    
        sum=sum+n*n
    
    return sum
    
print(calc(1,2,3))

list=[1,2,3,4]

#可变参数 入参可以*数组即可

print(calc(*list))

#关键字参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple

#关键字参数在函数内部自动组装为一个dict。请看示例：**参数

def person(name,age,**others):

    print('name:',name,'age:',age,'others:',others)
    
person('a',13,sex='girl',job='Engineer')

# 直接写参数不加引号,dict参数必须要有'',关键字参数**dict即可

extra={'sex':'girl','job':'Engineer'}

person('b',14,**extra)

#检查关键字函数是否存在某些参数

def person1(name,age,**others):

    if 'sex' in others:
    
        print('six')

    print('name:',name,'age:',age,'others:',others)
    
person1('a',13,sex='girl',job='Engineer')


#命名关键字参数:如果要限制关键字参数的名字，就可以用命名关键字参数,参数必须全部输入

def person2(name,age,*,sex,job):

    print('name:',name,'age:',age,sex,job)

person2('a',13,sex='girl',job='Engineer222')

#含有可变参数时,后面跟着的命名关键字参数不需要*

def person3(name,age,*agrs,sex,job):

    print('name:',name,'age:',age,sex,job,agrs)

person3('a',13,sex='girl',job='Engineer333',*list)

#命名关键字参数调用时必须有参数名,除非函数生命时参数设了缺省值

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a,b,c=1,*ags,e,**kw):

    print(a,b,c,ags,e,kw)

answer1=(1,2,3,4,5)

answer2={'e':'aaa','m':111,'n':212}

f1(*answer1,**answer2)

#so~对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

#递归函数

def fact(n):

    if n==1:
    
        return 1
        
    return n*fact(n-1)
    
print(fact(5))

#防止栈溢出:尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式

def fact1(n):

    return fact2(n,1)
    
def fact2(n,m):

    if n==1:
    
        return m
        
    return fact2(n-1,n*m)

print(fact1(3))

#练习汉诺塔 

def han(m):
    
    if m==1:
    
        return 1
    
    return 2*han(m-1)+1
    
print(han(64))
    
#退出

exit()