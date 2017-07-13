# 协程
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同,
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，
# 在适当的时候再返回来接着执行。协程的特点在于是一个线程执行

# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
# 因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
# 在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，
# 既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

#消费者
def consumer():
    s=''
    #在Python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False 
    while True:
        m=yield s
        if not m:
            return
        
        print('CONSUMER consumer %s' % m)
        
        s='200 OK'
    

#生产者
def produce(c):
    
    c.send(None)#启动生成器到第一个yield
    
    n=0
    
    while n<5:
        
        n=n+1
        result=c.send(n)
        
        print('PRODUCE produce %s' % n)
        
        print('PRODUCE consumer result %s' % result)
        
    c.close()#关闭
    
c=consumer()
produce(c)

# CONSUMER consumer 1
# PRODUCE produce 1
# PRODUCE consumer result 200 OK
# CONSUMER consumer 2
# PRODUCE produce 2
# PRODUCE consumer result 200 OK
# CONSUMER consumer 3
# PRODUCE produce 3
# PRODUCE consumer result 200 OK
# CONSUMER consumer 4
# PRODUCE produce 4
# PRODUCE consumer result 200 OK
# CONSUMER consumer 5
# PRODUCE produce 5
# PRODUCE consumer result 200 OK


# 注意到consumer函数是一个generator，把一个consumer传入produce后：

    # 首先调用c.send(None)启动生成器；

    # 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

    # consumer通过yield拿到消息，处理，又通过yield把结果传回；

    # produce拿到consumer处理的结果，继续生产下一条消息；

    # produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

# 最后套用Donald Knuth的一句话总结协程的特点：

# “子程序就是协程的一种特例。”