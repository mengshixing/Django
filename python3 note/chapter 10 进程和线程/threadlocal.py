#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#ThreadLocal在多线程环境下如何不传递参数

import threading
global_dict={}#定义一个全局dict

def std_thread(name):
    std=name
    global_dict[threading.current_thread()]=std
    
    do_task1()
    do_task2()
def do_task1():#不需要传入参数
    std=global_dict[threading.current_thread()]
    print('do_task1',std)
def do_task2():
    std=global_dict[threading.current_thread()]
    print('do_task2',std)
    
t1 = threading.Thread(target= std_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= std_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

glb=44
d={'a':1}
def testglb():
    glb=55 #修改的是新增的局部变量mutation（可变对象）
    d['b']=2 #修改的是全局变量rebinding（不可变对象）
    print(glb)
    print(d)
testglb()
print(glb)
print(d)

def testglb1():
	#在d = {}这句，它是”有歧义的“了，所以它是创建了局部变量d，
	#而不是引用全局变量d，所以d['c']=222也是操作的局部变量。
    d={}
    d['c']=222
    print(d)
testglb1()
print(d)

# 推而远之，这一切现象的本质就是”它是否是明确的“。

# 仔细想想，就会发现不止dict不需要global，所有”明确的“东西都不需要global。

# 因为int类型str类型之类的不可变对象，每一次操作就重建新的对象，

# 他们只有一种修改方法，即x = y， 恰好这种修改方法同时也是创建变量的方法，

# 所以产生了歧义，不知道是要修改还是创建。而dict/list/对象等可变对象，

# 操作不会重建对象，可以通过dict['x']=y或list.append()之类的来修改，

# 跟创建变量不冲突，不产生歧义，所以都不用显式global。


#下面使用ThreadLocal来做这件事 ThreadLocal是一个全局dict

local_sch=threading.local()
	
def sch_thread():
	sch=local_sch.school
	print('Hello, %s (in %s)' % (sch, threading.current_thread().name))

def process_thread(name):
	local_sch.school=name
	sch_thread()
	
t1 = threading.Thread(target= process_thread, args=('jack',), name='Thread1')
t2 = threading.Thread(target= process_thread, args=('rose',), name='Thread1')
t1.start()
t2.start()
t1.join()
t2.join()










