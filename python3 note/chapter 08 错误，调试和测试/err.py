#调用堆栈

import logging

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main(s):
    try:
        bar(s)
    except Exception as e:
        logging.exception(e)#记录下错误
    
main(0)

print('end')
#错误日志如下:一步步打印至错误原始调用

# Traceback (most recent call last):
  # File "err.py", line 8, in <module>
    # main(0)
  # File "err.py", line 7, in main
    # bar(s)
  # File "err.py", line 5, in bar
    # return foo(s)*2
  # File "err.py", line 3, in foo
    # return 10/int(s)
# ZeroDivisionError: division by zero

#抛出错误，自定义错误

class FuncaError(ValueError):
    pass
    
def foo(s):
    if s==0:
        raise FuncaError('funcerr %s' % s)
    return 10/int(s)
#foo(0)
print('continue')   


def bar():
	try:
		foo(0)
	except ValueError as e:
		print('ValueError!')
		raise#raise语句如果不带参数，就会把当前错误原样抛出,一直向上
bar()

#raise 可以转换错误类型
# except ValueError:
	# raise ZeroDivisionError('ZeroDivisionError')