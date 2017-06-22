#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#多进程 从本文开始在centos练习
#Unix/Linux提供了fork()调用,调用一次，返回两次,分别在父进程和子进程内返回

import os
print('Process (%s) start' % os.getpid())

pid=os.fork()
if pid==0:
    print('this is a child process %s,parent is %s' % (os.getpid(),os.getppid()))
else:
    print('%s just create a child %s' % (os.getpid(),pid))
    
#此时os.fork()值即os.getpid(),生成了一个父进程,并复制返回了一个子进程

#multiprocessing 跨平台的多进程服务程序
#multiprocessing模块提供了一个Process类来代表一个进程对象

from multiprocessing import Process
import os

def run_process(name):
    print('this is a child process %s(%s)' % (name,os.getpid())
    
if __name__=='__main__':
	
    print('parent process %s.' % os.getpid())
    
    #创建子进程
    #传入函数和参数
    p=Process(target=run_process,args=('test',))
    print('child start.')
    p.start()
    p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('child end.')