#错误处理 可以错误码来表示(缺点太多,错误情况可能很多)
def foo():
	r=code_list();
	if r==-1:
		return -1
	return r
def bar():
	r=foo()
	if r==-1:
		print('error')
	else:
		pass
def code_list():
	return -1
bar()

#try  处理异常

def tstry(division):
	print('try处理异常')
	try:
		print('try ...')
		r=10/int(division)
		print('result..',r)
	except ZeroDivisionError as e:#捕捉0异常
		print('ZeroDivisionError',e)
	except ValueError as e:#能同时捕捉多个异常
		print('ValueError',e)
	else:
		print('no error')#没有错误
	finally:
		print('finally..')
	print('end')

tstry(0)
tstry(2)
tstry('a')
#所有的错误类型都继承于BaseException

