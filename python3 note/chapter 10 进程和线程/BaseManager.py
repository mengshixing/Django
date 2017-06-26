#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#分布式进程
#在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以
#分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

#managers子模块还支持把多进程分布到多台机器上
import random,time,queue
from multiprocessing.managers import BaseManager

#发送队列
task_que=queue.Queue()
#接受队列
result_que=queue.Queue()

class QueueManager(BaseManager):
	pass

#注册到网络

def cal1():
	return task_que
def cal2():
	return result_que

QueueManager.register('get_task_que',callable=cal1)
QueueManager.register('get_result_que',callable=cal2)

#绑定端口设置验证码,启动
manager=QueueManager(address=('',1000),authkey=b'123')
manager.start()

task=manager.get_task_que()
result=manager.get_result_que()
for i in range(10):
	n=random.randint(0,10000)
	print(n)
	task.put(n)

#获取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=30)
    print(r)
# 关闭
manager.shutdown()
print('master exit.')


# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
# 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加






