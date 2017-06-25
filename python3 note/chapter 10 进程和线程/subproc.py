#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#子进程,subprocess模块可以启动一个子进程,控制其输出输入
import subprocess
print('$ nslookup www.python.org')

#subprocess.call('脚本/shell', shell=True)

r=subprocess.call(['nslookup','www.python.org'])
print('exit code:',r)

#如果子进程还需要输入，则可以通过communicate()方法输入

print('$ nslookup')

# Popen.stdin：如果在创建Popen对象是，参数stdin被设置为PIPE，
# Popen.stdin将返回一个文件对象用于策子进程发送指令。否则返回None。
# Popen.stdout：如果在创建Popen对象是，参数stdout被设置为PIPE，
# Popen.stdout将返回一个文件对象用于策子进程发送指令。否则返回None。
# Popen.stderr：如果在创建Popen对象是，参数stdout被设置为PIPE，
# Popen.stdout将返回一个文件对象用于策子进程发送指令。否则返回None。
p=subprocess.Popen(['nslookup'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Popen.communicate(input=None)：与子进程进行交互。
# 向stdin发送数据，或从stdout和stderr中读取数据。
# 可选参数input指定发送到子进程的参数。
# Communicate()返回一个元组：(stdoutdata, stderrdata)。
# 注意：如果希望通过进程的stdin向其发送数据，在创建Popen对象的时候，
# 参数stdin必须被设置为PIPE。同样，如果希望从stdout和stderr获取数据，
# 必须将stdout和stderr设置为PIPE。

output,err=p.communicate(b' set q=mx\npython.org\nexit\n')

print(output.decode('utf-8'))
# Popen.returncode：获取进程的返回值。如果进程还没有结束，返回None。
print('Exit code:',p.returncode)

#http://hackerxu.com/2014/10/09/subprocess.html

# subprocess.PIPE实际上为文本流提供一个缓存区。
# 直到communicate()方法从PIPE中读取出PIPE中的文本.要注意的是，
# communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成。

#进程间通信

from multiprocessing import Process,Queue
import os,time,random

#写数据进程
def write(q):
    print('Process write %s' % os.getpid())
    for i in ['A','B','C']:
        print('put %s to queue' % i)
        q.put(i)
        time.sleep(random.random())

#读数据进程
def read(q):
    print('Process read %s' % os.getpid())
    while True:
        value=q.get(True)
        print('get %s form queue' % value)
        
if __name__=='__main__':

    q=Queue()
    

    pwrite=Process(target=write,args=(q,))
    pread=Process(target=read,args=(q,))
    pwrite.start()
    
    pread.start()
    #等待pwrite结束
    pwrite.join()
    #pread进程里是死循环，无法等待其结束，只能强行终止:
    pread.terminate()
    
    
























