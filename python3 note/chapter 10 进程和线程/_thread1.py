#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#多线程
#_thread和threading模块(分别是低级/高级模块)
#大多数时候用threading

import time,threading

def loop():
    print('thread %s is running' % threading.current_thread().name)
    
    for i in range(5):
        print('%s %s' % (i,threading.current_thread().name))
        time.sleep(1)
    
    print('thread end %s' % threading.current_thread().name)
  
#打印主线程,名字默认MainThread  
print('start %s' % threading.current_thread().name)

#启动子线程,名字为loopthread
t=threading.Thread(target=loop,name='loopthread')

t.start()
t.join()

print('end %s' % threading.current_thread().name)

#下面看下多线程可以同时操作一个变量

flag=0
def change_f(n):
    global flag;#将flag声明卫全局变量   
    flag=flag+n
    flag=flag-n

def run_change(n):
    for i in range(100000):#多次执行,cpu切片
        change_f(n)

thread1=threading.Thread(target=run_change,args=(3,))
thread2=threading.Thread(target=run_change,args=(6,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#高级语言的一条语句在CPU执行时是若干条语句，
#即使一个简单的计算：flag=flag+n,也分为2步
#1计算flag+n存入临时变量,
#2将临时变量的值赋给flag
#正常状况下:
# flag=0

# thread1:    x1=flag+3    flag=0
# thread1:    flag=x1      flag=3
# thread1:    x1=flag-3    flag=3
# thread1:    flag=x1      flag=0

# thread2:    x2=flag+6    flag=0
# thread2:    flag=x2      flag=6
# thread2:    x2=flag-6    flag=6
# thread2:    flag=x2      flag=0
# 切片次数过多时,有可能

# thread1:    x1=flag+3    flag=0
# thread1:    flag=x1      flag=3


# thread2:    x2=flag+6    flag=3
# thread2:    flag=x2      flag=9
# thread2:    x2=flag-6    flag=9

# thread1:    x1=flag-3    flag=9
# thread1:    flag=x1      flag=6

# thread2:    flag=x2      flag=6
print(flag) #输出了6或者-3等等

#因此需要加锁lock
flag1=0
lock=threading.Lock()
def change_f1(n):
    global flag;#将flag声明卫全局变量   
    flag=flag+n
    flag=flag-n

def run_change1(n):
    for i in range(100000):#多次执行,cpu切片
        lock.acquire()#取得锁
        try:            
            change_f(n)
        finally:
            lock.release()#最后一定要释放锁

thread3=threading.Thread(target=run_change,args=(3,))
thread4=threading.Thread(target=run_change,args=(6,))

thread3.start()
thread4.start()

thread3.join()
thread4.join()
print(flag1)#结果一定是0

import multiprocessing
print(multiprocessing.cpu_count())









        