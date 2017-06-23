#文档测试
import re
#断言匹配含abc开始的def
m = re.search('(?<=abc)def', 'abcdef')
#打印匹配到的第一个def
print(m.group(0))


def abs(n):
    '''
    function to get absolut value of number 
    
    example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n>=0 else (-n)
    
#dict
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
#练习fact(n)
def fact(n):
    '''
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    '''
    if n<1 :
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)
        
#fact(0)
        

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
    
    
    
    
    
    
    
    