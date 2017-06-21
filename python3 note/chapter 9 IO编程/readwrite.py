#读写，python 内置读写与c用法兼容

#读文件模式打开,文件找不到会抛IOError
f=open('a.txt','r',encoding='utf8',errors='ignore')

#读文件,
#字符编码不设置的话,可能会抛UnicodeDecodeError
s=f.read()
print(s)

f.close()

#为了保证出IOError也能正常关闭文件,使用try

try:
    f=open('a.txt','r',encoding='utf8',errors='ignore')
    s=f.read()
    print(s)
finally:
    if f:
        print(f)
        f.close()
        
#这种写法不够简洁,python引入了with来自动调用close方法

with open('a.txt','r',encoding='utf8',errors='ignore') as f:
    print(f.read())
    
#read()一次读取全部
#read(size)一次读取多少字节
#readline()一次读取一行
#readlines()一次读取全部按行生成list返回

with open('a.txt','r',encoding='utf8',errors='ignore') as f:
    #print(f.readline())
    #print(f.readlines())
    print(f.read(5))
    
#flie-like Object,像open()函数返回的这种有个read()方法的对象
#包括file,内存的字节流，网络流，自定义流,StringIO等

#二进制文件,不能有errors参数
with open('bg.gif','rb') as f:
    print(f.read())

#写文件与读类似,传入'w'或者'wb'标识
#使用with 可以保证close()执行(此时会将缓存写入文件)
with open('a.txt','w',encoding='utf8',errors='ignore') as f:
    f.write('gg ___,___')
    
#StringIO,在内存中读写str

from io import StringIO

f=StringIO()
f.write('hello')
f.write(' ')
f.write('xiao8')
print(f.getvalue())

g=StringIO('a\nbb bb\n ccc ')
while True:
    s=g.readline()
    if s=='':
        break
    print(s.strip())#去除首尾空格

#BytesIO,操作二进制数据

from io import BytesIO
f=BytesIO()
f.write('kai开心'.encode('utf-8'))#utf-8,utf8都可以
print(f.getvalue())


h=BytesIO(b'kai\xe5\xbc\x80\xe5\xbf\x83')#注意此处b开头
print(h.read())

#操作文件好目录,os模块

import os
print(os.name)#nt是Windows系统,posix:系统是Linux、Unix或Mac OS X

#print(os.uname())获取系统详细,windows不支持

print(os.environ)#打印环境变量

print(os.environ.get('PATH'))#获取某个环境变量的值

#当前绝对路径
print(os.path.abspath('.'))

#创建新目录

#新目录完整路径 
#r默认不转义
#os.path.join在windows时返回\路径,Linux时/
print(os.path.join(r'E:\123\Django\python3 note\chapter 9 IO编程', 'testdir'))
#创建目录 
os.mkdir(r'E:\123\Django\python3 note\chapter 9 IO编程\testdir')
#删除
os.rmdir(r'E:\123\Django\python3 note\chapter 9 IO编程\testdir')

#os.path.split()把一个路径拆分为两部分
#后一部分总是最后级别的目录或文件名

print(os.path.split(r'E:\123\Django\python3 note\chapter 9 IO编程\a.txt'))

#os.path.splitext()获取扩展名
print(os.path.splitext(r'E:\123\Django\python3 note\chapter 9 IO编程\a.txt'))

#拼接函数只是操作字符串,文件/路径不存在也能执行 
#aaaaaa.txt并不存在
print(os.path.splitext(r'E:\123\Django\python3 note\chapter 9 IO编程\aaaaaa.txt'))

#重命名
#print(os.rename('a.txt', 'b.txt'))
#移除
#os.remove('b.txt')

#shutil模块提供了copyfile()等函数可以复制文件等

#列出当前目录

print(os.path.isdir(r'E:\123\Django\python3 note'))
print([x for x in os.listdir(r'E:\123\Django\python3 note')])
#注意的是join r'路径'最后不要加\
print([x for x in os.listdir(r'E:\123\Django\python3 note') if os.path.isdir(os.path.join(r'E:\123\Django\python3 note',x))])

#列出'chapter 8 错误，调试和测试'目录下的py文件

print([x for x in os.listdir(r'E:\123\Django\python3 note\chapter 8 错误，调试和测试') if os.path.splitext(x)[1]=='.py'])

#练习1利用os模块编写一个能实现dir -l输出的程序。

#写在dir_l.py文件里
#引用它的方法即可
import dir_l
dir_l.dir_l(r'E:\123\Django\python3 note')

#练习2,在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

#本示例在windows下
def Seachkey(d,key):
    for x in os.listdir(d):
        if os.path.isdir(os.path.join(d,x)):
            Seachkey(os.path.join(d,x),key)
        else:
            if key in x:
                print(x)
Seachkey(r'E:\123\Django\python3 note','d')


