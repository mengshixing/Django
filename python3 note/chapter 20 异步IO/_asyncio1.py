# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

import asyncio
import threading

#@asyncio.coroutine把一个generator标记为coroutine类型:协程类型
@asyncio.coroutine
def hello():
    print('a ---- %s' % threading.currentThread())
    
    yield from asyncio.sleep(3)
    
    print('b ---- %s' % threading.currentThread())
  
  
# 1 hello()会首先打印a，

# 2 然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()
# 也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。

# 3 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

# 把asyncio.sleep(3)看成是一个耗时3秒的IO操作，在此期间，主线程并未等待，
# 而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
  
  

#一个EventLoop的引用 
loop=asyncio.get_event_loop()

#执行协程
loop.run_until_complete(hello())
#loop.close()#关闭

# 输出一个线程
# a ---- <_MainThread(MainThread, started 244352)>
# b ---- <_MainThread(MainThread, started 244352)>

#多任务时更明显

#一个EventLoop的引用 
loop1=asyncio.get_event_loop()
task=[hello(),hello(),hello()]
#执行协程
loop1.run_until_complete(asyncio.wait(task))
loop1.close()#关闭

#输出一个线程  4个任务
# a ---- <_MainThread(MainThread, started 90668)>
# b ---- <_MainThread(MainThread, started 90668)>

# 第二个task输出
# a ---- <_MainThread(MainThread, started 90668)>
# a ---- <_MainThread(MainThread, started 90668)>
# a ---- <_MainThread(MainThread, started 90668)>
# b ---- <_MainThread(MainThread, started 90668)>
# b ---- <_MainThread(MainThread, started 90668)>
# b ---- <_MainThread(MainThread, started 90668)>


