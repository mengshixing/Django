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

