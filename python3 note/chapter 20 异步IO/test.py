#test.py

def h():
    print('To be brave')
    yield 5
    print('To be brave2')
c=h()

# c.__next__()
#此时不会输出打印语句,http://www.jb51.net/article/15717.htm

# Python2.5以前，yield是一个语句，但现在2.5中，yield是一个表达式(Expression)，比如：
# m = yield 5 表达式(yield 5)的返回值将赋值给m，所以，认为 m = 5 是错误的。

# print(c.__next__()) #To be brave  5
# print(c.__next__()) #StopIteration


# end(msg) 与 next()
# 了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。
# 其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，
# 而next()不能传递特定的值，只能传递None进去。因此，我们可以看做

# c.next() 和 c.send(None) 作用是一样的。
# 需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，
# 否则会出错的，因为没有yield语句来接收这个值。
def m():
    print('To be brave')
    m = yield 5
    print(m)
    print('To be brave2')
l=m()

#print(l.__next__()) # To be brave 5 此时返回了5yield 表达式返回了5
#print(l.__next__()) # None  To be brave2 StopIteration  此时m值为None

# print(l.send(None)) # To be brave 5 此时返回了5yield 表达式返回了5
# send()可以传递yield表达式的值进去，
# print(l.send('haha')) # None  To be brave2 StopIteration  此时m值为haha

# throw() 与 close()中断 Generator
# 中断Generator是一个非常灵活的技巧，可以通过throw抛出一个GeneratorExit异常来终止Generator。
# Close()方法作用是一样的，其实内部它是调用了throw(GeneratorExit)的。我们看：
def close(self):
    try:
        self.throw(GeneratorExit)
    except (GeneratorExit, StopIteration):
        pass
    else:
        raise RuntimeError("generator ignored GeneratorExit")
# Other exceptions are not caught
# 因此，当我们调用了close()方法后，再调用next()或是send(msg)的话会抛出一个异常：
# Traceback (most recent call last):
  # File "/home/evergreen/Codes/yidld.py", line 14, in <module>
    # d = c.send('Fighting!')  #d 获取了yield 12 的参数值12
# StopIteration

l.close()
l.__next__()