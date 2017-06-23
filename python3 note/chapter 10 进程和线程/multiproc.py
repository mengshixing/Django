#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#multiprocessing 跨平台的多进程服务程序
#multiprocessing模块提供了一个Process类来代表一个进程对象

from multiprocessing import Process
import os

def run_process(name):
    print('this is a child process %s(%s)' % (name,os.getpid()))
    
if __name__=='__main__':

    print('parent process %s.' % os.getpid())
    
    #创建子进程
    #传入函数和参数
    p=Process(target=run_process,args=('test',))
    print('child start.')
    p.start()
    p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('child end.')