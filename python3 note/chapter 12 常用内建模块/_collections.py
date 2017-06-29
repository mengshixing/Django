#collections集合模块

#namedtuple是一个函数,用来创建tuple对象
#并且规定了tuple元素的个数,并可以用属性而不是索引来引用tuple的某个元素
point=(2,3)
print(point)
from collections import namedtuple

Point=namedtuple('_Point',['x','y'])
p=Point(2,4)
print(p.x,p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
# namedtuple('名称', [属性list]):
# Circle=namedtuple('Circle',['x','y','r'])圆心坐标,半径表示一个圆

#deque特殊的list,插入和删除元素效率高,适合用于队列和栈
from collections import deque
l_deque=deque(range(10))
print(l_deque)
l_deque.pop()
l_deque.append('A')
l_deque.appendleft('B')#左侧添加元素
l_deque.appendleft('C')
l_deque.popleft()#左侧删除元素
print(l_deque)

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。
#如果希望key不存在时，返回一个默认值，就可以用defaultdict

from collections import defaultdict
#默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

d_dict=defaultdict(lambda :'key is not exist !')
d_dict['s']=999
print(d_dict['s'])
print(d_dict['n'])

#OrderedDict有序dict

from collections import OrderedDict
d1={'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d1)#{'Tracy': 85, 'Michael': 95, 'Bob': 75}无序
print(isinstance(d1,dict))
d2=OrderedDict([('Michael', 95), ('Bob', 75), ('Tracy', 85)])
print(d2)
#有序且按ket插入顺序排列
d2['B']=222
d2['c']='www'
print(d2.keys())

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

class FIFOdict(OrderedDict):
    def __init__(self,maxnub):
        super(FIFOdict,self).__init__()#调用下一个mro
        self._maxnub=maxnub
    def __setitem__(self,key,value):
        #相当于if key in self: containskey=1 else: containskey=0
        isexist=1 if key in self else 0
        
        if len(self)-isexist>=self._maxnub:
            last=self.popitem(last=False)
            print('last',last)
        if isexist:
            del self[key]:
            print('set:',(key,value))
        else:
            print('add:',(key, value))
        OrderedDict.__setitem__(self, key, value)
        



#Counter一个dict
#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for i in 'dadwqmnqf[q qr jq] qjfqof qo ':
    c[i]=c[i]+1
print(c)
#Counter({'q': 8, ' ': 5, 'f': 3, 'd': 2, 'j': 2, 'o': 2, 
#'a': 1, ']': 1, '[': 1, 'n': 1, 'r': 1, 'm': 1, 'w': 1})








