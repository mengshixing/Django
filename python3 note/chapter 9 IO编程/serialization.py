#序列化 把变量从内存中变成可存储或传输的过程称之为序列化,在Python中叫pickling
#引入pickle模块

import pickle

d=dict(name='wangjie',age=33,sex='男')

#pickle.dumps()方法把任意对象序列化成一个bytes
#pickle.dump()方法写入文件
print(pickle.dumps(d))

with open('d.txt','wb') as f:
    pickle.dump(d, f)
    
#pickle.loads()反序列化出对象
#pickle.load()可以直接从file-like Object中反序列化出对象

with open('d.txt','rb') as f:
    print(pickle.load(f))
    
#JSON
#JSON比XML更快，而且可以直接在Web页面中读取
# JSON类型    Python类型
# {}          dict
# []          list
# "string"    str
# 1234.56     int或float
# true/false  True/False
# null        None

import json

#dumps()方法返回一个str，内容就是标准的JSON
#类似的，dump()方法可以直接把JSON写入一个file-like Object

print(json.dumps(d))

with open('d.txt','w') as f:
    json.dump(d, f)
    
#同样的要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
#前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

with open('d.txt','r') as f:
    print(json.load(f))
    
#JSON进阶

class Stu():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
s=Stu('lan',19)
#json.dumps不能直接转换类


def stu_dic(stu):
    return {
        'name':stu.name,
        'age':stu.age   
    }


print(stu_dic(s))

print(json.dumps(s,default=stu_dic))

#或者直接调用类的__dict__属性

print(json.dumps(s,default=lambda x:x.__dict__))

#同样的反序列化 
s=json.dumps(s,default=lambda x:x.__dict__)
#反序列化成了dic
print(json.loads(s))

#如果要反序列成类，定义新方法
def js_dic(d):
	return Stu(d['name'],d['age'])
	
print(json.loads(s,object_hook=js_dic))















