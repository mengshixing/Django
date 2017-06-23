#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#子进程,subprocess模块可以启动一个子进程,控制其输出输入
import subprocess
print('$ nslookup www.python.org')

r=subprocess.call(['nslookup','www.python.org'])
print('exit code:',r)