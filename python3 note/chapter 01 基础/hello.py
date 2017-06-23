# 输入输出

name=input()

print('hello',name)

# 字符串加\转义  r'' 表示''内部的内容不转义

print('i\'m \"ok\"!')

# 空值None,常量大写

#除法 //地板除

print(10/3,10//3);

#字符串编码 unicode编码的默认  ord()函数获取字符的整数表示,chr()把编码转化为对应的字符

print (ord('A'))

print (chr(25991))

#字符串编码  b'' 表示byte编码  decode()方法可以将bytes变为str  len()字符的长度

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('中国'),len('中国'.encode('utf-8')))

#占位符 %d 整数  %f 小数 %s 字符串  %x 十六进制   %3d 表示占3个位宽   %03d 表示至少补齐3位  %.2f小数点保留2位

#字符串中的%可以用%%来表示  type()来获取变量类型

print('%3d' % 22,'%03d' % 22)

#练习：

#小明的成绩从72分提升到了85分,计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位

print(type((85-72)/72))

print('小明成绩提升了%.1f%%' % ((85-72)*100/72))


#有序集合list  len()长度 append()添加元素到最后  insert()插入指定位置

list1=['jack','lili','lucy']

print(len(list1),list1[0],list1[-1])

list1.append('lilei')

list1.insert(1,'hanmeimei')

print(list1)

#list 删除元素pop() 删除指定位置 默认最后一个

list1.pop();

list1[2]=['aa',123]

print(list1); print(list1[2])

#tuple 类似与list 一旦初始化 就不能再修改了 tuple只有1个元素时，为防止歧义需加,

tuple1=('jack','lili','lucy') 

tuple2=(1); tuple3=(1,)

print(tuple1,tuple2,tuple3)

#tuple 元素指向的元素是可以改变的

tuple4=('jack','lili','lucy',[123,'abc']); print(tuple4)

tuple4[3][1]='changed'; print(tuple4)

#练习

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0],L[1][1],L[2][2])

#if语句 if x: 只要x是非零数值,非空字符串,非空list就为True,否则False

birth=int(input('birth:'))

if birth>2000:

    print('00后')

#练习：

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''

s=80.5/(1.75*1.75)

print(s);

if s>32:

    print('严重肥胖')

elif s>=28:

    print('肥胖')

elif s>=25:

    print('过重')

elif s>=18.5:

    print('正常')

else:

    print('肥胖')

#循环 ,for while break continue 常规用法

names = ['Michael', 'Bob', 'Tracy']

for name in names:
    
    print(name)

#range()函数，可以生成一个整数序列 

s=0

for x in range(101):

    s=s+x

print(s)

n=100

while n>0:

    s=s-n;n=n-1

print(s)

#dict python的字典类型 key in dict判断是否存在 dict.get('key',value)key不在时赋值

d={'a':123,'b':'aaa',3:'aa'}

print(d[3]); print('b' in d); print(d.get('a'))

print(d.get('a',456)); print(d.get('c')); print(d.get('c',456))

#set 类似dict,但是不存value且key不重复

s=set([1,1,2,2,3,4]); print(s)

s.add(7); print(s)

s.remove(2); print(s)

s2=set([4,8,9]); print(s&s2); print(s|s2);

# 再议不可变对象

key=(1,2,3); key1=(1,[2,3])

d[key]=1111; 

d['dd']=key; 

#d[key1]=1111;  不可以做key哦！TypeError: unhashable type: 'list'

#可以做value

d['dd']=key1; 

print(d)

s.add(key)

#s.add(key1) 不可以做key哦！TypeError: unhashable type: 'list'

print(s)

#综上所述 tuple虽然不可变对象,含有引用元素list后不能再作为key了

#退出

exit()
