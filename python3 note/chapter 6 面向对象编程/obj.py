#class object 定义类
class Student(object):
    pass
#表示类是继承object的
stu=Student()
print(stu)
print(Student)

stu.name='kej'
print(stu.name)

#创建实例时,可以强制绑定一些属性,初始化时候必须的参数
class Student1(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    pass

stu1=Student1('s',2)
print(stu1.name)

#数据封装
class Student2(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print1(self):
        print('%s: %s' % (self.name,self.age))
    def getgrade(self):
        if(self.age>90):
            return 'A'
        else:
            return 'B'
stu2=Student2('ZHANG',92)
stu2.print1()
print(stu2.getgrade())

#访问限制,如果让内部属性不在外面访问可以加__变成私有变量private
class Student3(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def print(self):
        print('%s :%s' % (self.__name,self.__age))
stu3=Student3('li',80)
stu3.print()
#print(stu3.__name)

#提示stu3没有__name属性,因为python解释器把__name解释成了_Student3__name
print(stu3._Student3__name)

#添加get,set方法来提供外部访问
class Student4(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        if 0<age<200:
            self.__age=age
        else:
            raise ValueError('bad age')
    def print(self):
        print('%s :%s' % (self.__name,self.__age))
        
stu4=Student4('kaikai',333) 
stu4.print()
stu4.set_name('haihai')
print(stu4.get_name())
        
#stu4.set_age(222)      
#继承和多态
class Animal(object):
    def run(self):
        print('Animal run')
class dog(Animal):
    def run(self):
        print('dog run')
class Cat(Animal):
    def eat(self):
        print('Cat eat')    
a=Animal()
d=dog()
c=Cat()
a.run()
d.run()
c.run()

print(isinstance(d,Animal))
print(isinstance(a,dog))        
        
def runanimal(Animal):
    Animal.run()
    Animal.run()
        
runanimal(a)       
runanimal(d)            
runanimal(c)           
 
#静态语言 vs 动态语言
#前者如java需要传入一个Animal或者她的子类
#后者python只需要传入一个有run方法的对象即可

class Timer(object):
    def run(self):
        print('start')

runanimal(Timer()) 

#获取对象信息

print(type('124'))
print(type(-1))
print(type(None))

print(type(abs))
print(type(a))

print(type('a')==str)
print(type('a')==type('123'))
print(type('a')==type(123))

#types可以判断函数
print('types start')
import types
print(type(runanimal)==types.FunctionType)
print(type(runanimal)==types.BuiltinFunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

#使用isinstance()也能判断type判断的基本类型,也能判断类继承

print('isinstance start')
print(isinstance('123',object))

#使用isinstance()也还可以判断一个变量是否是某些类型中的一种，

print(isinstance('aaa',(int,str)))
#使用dir可以获取对象的所有方法和属性
print(dir('isinstance start'))
print('isinstance start'.__len__())
print('isinstance start'.__add__('22'))

#例如__len__就是读取对象的该方法

class tsobj(object):
    def __len__(self):
        return 100

print(len(tsobj()))

#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class testobj(object):
    def __init__(self):
        self.x=9
    def power(self):
        return x*x

o=testobj()      
print(hasattr(o,'x'))
print(hasattr(o,'y'))
setattr(o,'y','3')
print(hasattr(o,'y'))
print(getattr(o,'x'))


#print(getattr(o,'z')) 判断属性存在的时候可以加第三个参数

print(getattr(o,'z',404))
        
print(getattr(o,'x',404))        
  
#示例  
def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None

#实例属性和类属性

class ts(object):
	name="classname"
	
s=ts()
s.name="objectname"
print(s.name)
print(ts.name)
del s.name
print(s.name)
    
        