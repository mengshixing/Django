#调试 
#1使用print()打印 坏处是发布时候还要删除
#2断言 assert

def foo(n):
	assert n!=0,'n is zero'#断言n!=0为True
	return 10/n
	
#foo(0)

#断言失败,输出AssertionError: n is zero
#断言比print好在python解释器可以 python -O debug.py
#此时assert语句等同于pass

#3 logging
import logging

#logging级别debug,info,error,warning等 指定一个时,其他不会打印
#logging可以配置同时输出到文件,console等
logging.basicConfig(level=logging.INFO)
s=0
logging.info('s=%s' % s)

print('log当前级别是info')

#4 pdb 参见pdberr.py
