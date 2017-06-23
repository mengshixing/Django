#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'test module'

__author__='meng'
import sys

def hello():
    args=sys.argv
    if len(args)==1:
        print('hello,world')
    elif len(args)==2:
        print('hello,%s' % args[1])
    else:
        print('too many args')

if __name__=='__main__':
    hello()
	
#第三行模块注释,系统模块sys.argv用list存储了命令行的所有参数python test.py时有一个参数'test.py'
#python test.py zhang时有2个参数'test.py','zhang'

#if __name__=='__main__':运行该模块时执行成功,引入时判断失败