#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time,sys,queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
	pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字	
QueueManager.register('get_task_que')
QueueManager.register('get_result_que')

server='127.0.0.1'

m=QueueManager(address=(server,99),authkey=b'123')

m.connect()

task=manager.get_task_que()
result=manager.get_result_que()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=30)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')