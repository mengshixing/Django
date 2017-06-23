#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用进程池批量创建子进程

from multiprocessing import Pool
import os,time,random

def time_proc(name):
    print('run task %s(%s)' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)#方法返回随机生成的一个实数，它在[0,1)范围内
    end=time.time()#返回时间戳,当前时间戳为: 1459994552.51
    print('task run %0.2f' % (start-end))
    
if __name__=='__main__':
    print('Parent process start %s' % os.getpid())
    p=Pool(4)
	#Pool的默认大小是CPU的核数,0，1，2，3同时启动
	#4是最早结束的,接着运行4
    for i in range(5):
        p.apply_async(time_proc,args=(i,))
    print('waiting for subprocess done')
    p.close()
    p.join() #Pool调用Join之前会等待所有子进程结束
    print('all process done')



