#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time,sys,Queue#在2.x系列下使用Queue，3.x使用queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
	pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字	
QueueManager.register('get_task_que')
QueueManager.register('get_result_que')

server='192.168.0.115'

m=QueueManager(address=(server,1000),authkey=b'123')

m.connect()

task=m.get_task_que()
result=m.get_result_que()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=30) #获取发送队列
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)#放入结果队列
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')