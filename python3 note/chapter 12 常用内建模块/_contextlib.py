#contextlib上下文对象

#之前学到with打开文件不用担心资源未关闭
with open('bg.gif','rb') as f:
    print(f.read(10))
    
#实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句
#实现上下文管理是通过__enter__和__exit__这两个方法实现的

class test_contextlib():
    def __enter__(self):
        print('enter')
    def __exit__(self,exc_type,exc_value,traceback):
        print('exit')

with test_contextlib() as q:
    print(111)
        
#编写__enter__和__exit__仍然很繁琐，引入@contextmanager

from contextlib import contextmanager

class test_contextlib1():
    pass
@contextmanager
def test():
    print('enter')
    print(2222)
    yield
    print('exit')

with test() as t:
    print(333)

# 输出    
# enter
# 2222
# 333
# exit

#@contextmanager这个decorator(装饰器)接受一个generator(生成器)
#执行顺序如下
# 1 执行yield之前语句
# 2 执行with 语句
# 3 执行yield之后语句

@contextmanager
def html5(item):
    print('<%s>' % item)
    yield
    print('</%s>' % item)

with html5('div') as q:
    print('hello world !')

#@closing如果一个对象没有上下文,可以用closing()方法转换一下.等价于

# @contextmanager
# def closing(action):
	# try:
		# yield thing
	# finally:
		# thing.close()
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('http://www.baidu.com/')) as page:
	for line in page:
		print(line)

#打印了百度首页的源文件








	
	