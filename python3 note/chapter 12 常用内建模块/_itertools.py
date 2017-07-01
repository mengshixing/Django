#itertools提供了非常有用的操作迭代对象的函数
import itertools

#count()会创建一个无限的迭代器，Ctrl+C退出。
t_count=itertools.count(10)#从10开始,依次加1

# for i in t_count:
    # print(i)

#cycle()会把传入的一个序列无限重复下去：

t_cycle=itertools.cycle('chun')

# for i in t_cycle:
    # print(i)
    
#repeat()负责把一个元素无限重复下去,不过如果提供第二个参数就可以限定重复次数

t_repeat=itertools.repeat('quit0',3)
for i in t_repeat:
    print(i)
    
#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数
#根据条件判断来截取出一个有限的序列：
#itertools.takewhile(predicate, iterable),
#创建一个迭代器，生成iterable中predicate(item)为True的项，
#只要predicate计算为False，迭代就会立即停止。

for i in itertools.takewhile(lambda x:x<=20,t_count):
    print(i)#输入10到200
    
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for i in itertools.chain('ABC','XYZ','OPQ'):
    print(i)
    
#groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key,groups in itertools.groupby('wqnrqrqiiiiqoqowriiiiqahHhha',lambda x:x.upper()):
    print(key,list(groups))

#输出
# W ['w']
# Q ['q']
# N ['n']
# R ['r']
# Q ['q']
# R ['r']
# Q ['q']
# I ['i', 'i', 'i', 'i']
# Q ['q']
# O ['o']
# Q ['q']
# O ['o']
# W ['w']
# R ['r']
# I ['i', 'i', 'i', 'i']
# Q ['q']
# A ['a']
# H ['h', 'H', 'h', 'h']
# A ['a']


# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
