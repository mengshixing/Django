#class object 类绑定方法,实例绑定方法
class Student(object):
    pass

stu=Student()
stu.name='kejie'
print(stu.name)

#给实例绑定方法
def set_name(self,name):
    self.name=name    
    
from types import MethodType
stu2=Student()
stu2.set_name=MethodType(set_name,stu2)
stu2.set_name('222')
print(stu2.name)

#给类绑定方法

Student.set_name=set_name
stu3=Student()
stu3.set_name('333')
print(stu3.name)

#使用__slots__来限制实例能添加的属性

class Teacher(object):
    __slots__=('name')
    pass
te=Teacher()
te.name='aaa'
#te.age=2  会提示没有age属性
#对于子类实例,限制会失效
class ter(Teacher):
    pass
te2=ter();
te2.age=4
print(te2.age)

#设置实例属性添加限制
class Student1(object):
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<age<200:
            self.__age=age
        else:
            raise ValueError("bad values")
s=Student1()
s.set_age(11)

#python提供了@property装饰器可以把方法变成属性调用,上面的Student1类可以修改为:

class Student2(object):
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if 0<age<200:
            self.__age=age
        else:
            raise ValueError("bad values")
    
    @property
    def name(self):
        return self.__age
s2=Student2()
s2.age=66

#上面get方法可以直接用@property,同时生成了一个setter方法.
#只定义get的为只读属性

s3=Student2()
#print(s3.name) 此时报错
s3.age=99
print(s3.name)

#s3.name=222  报错 属性只读
 
#练习:请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):   
    # def __init__(self,width,height):
        # self.__width=width
        # self.__height=height 
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        if width<0:
            raise ValueError("bad values")
        self.__width=width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        if height<0:
            raise ValueError("bad values")
        self.__height=height        
    
    @property
    def resolution(self):
        return self.__width*self.__height
        
#sc=Screen(33,-10)
sc=Screen()
sc.width=33
sc.height=44
print(sc.resolution)

#python多重继承,有相同方法时遵循从前往后的规则

class Animal():
    def do(self):
        print('animal')
class Bird():
    def do(self):
        print('bird')
    def run(self):
        print('bird run')
class Parrot(Animal,Bird):
    pass
p=Parrot()
p.do()
p.run()

#关于定制类,__slots__能限制实例能添加的属性,
#__xxx__这种格式的变量和函数一般有特殊意义

class Personal():
    def __init__(self,name):
        self.__name=name
print(Personal('xiaoy'))

#__str__使用优化输出,__repr__用于调试显示
class Personal1():
    def __init__(self,name):
        self.__name=name
    def __str__(self):
        return "Personal1 object :(name : %s)" % self.__name
    __repr__=__str__
print(Personal1('xiaoy'))
Personal1('xiaoyy')

#__iter__使一个类可以for in 循环,__next__调用

class Fibseries():
    def __init__(self):
        self.a,self.b=1,2
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a
    
    #此时类虽然可以for循环,但是不能当list使用,需要__getitem__()方法  
    #__getitem__()方法传入参数可能有多种,int或者切片
    def __getitem__(self,n):
        a,b=1,1
        if isinstance(n,int):
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):#切片类型
            start=n.start
            stop=n.stop
            l=[]
            for x in range(stop):
                if x>=start:
                    a,b=b,a+b
                    l.append(a)
            return l
                
    
        
for n in Fibseries():
    print(n)

print(Fibseries()[3])
print(Fibseries()[13])

print(Fibseries()[1:10])

#与__getitem__对应的还有__setitem__和__delitem__把对象看成dict,赋值/删除

#__getattr__可以动态返回一个属性

class Getitemtest():
    def __init__(self):
        self.name='zhangsan'
    def __getattr__(self,attr):
        if attr=='age':#添加属性
            return 89
        if attr=='weight':#添加方法
            return lambda :25
        #raise AttributeError('\'getitemtest\' don\'t has attr %s' % attr)
        #修改默认返回的None
g=Getitemtest()
print(g.name)
print(g.age)
print(g.sex)#None,不会返回'has no attribute'因为__getattr__默认返回None
print(g.weight())
print(g.sex)

#应用链式调用

class Chain(object):
    def __init__(self,path=''):
        self.__path=path
    def __getattr__(self,path):#返回类本身,递归
        return Chain('%s/%s' % (self.__path,path))
    def __str__(self):
        return self.__path
    __repr__=__str__
    
print(Chain().staus)
print(Chain().staus.list)

#__call__方法对实例可以直接调用

class Callts():
    def __init__(self,name):
        self.__name=name
    def __call__(self):
        print('my name is %s' % self.__name)

cts=Callts('Lisa')
cts()

#__call__还可以定义参数,实例调用可以看成函数,实例函数无本质区别
#使用Callable可以判断一个对象能否被调用

print(callable(Callts('zhangsan')))#true

print(callable(Getitemtest()))#false

print(callable(abs))#true

#定制类#print(Chain().user('zhangsan').userinfo)变成GET /users/:user/userinfo API

class Getapi(object):
    def __init__(self,path='get'):
        self.__path=path
    def __getattr__(self,path):
        return Getapi('%s/%s' % (self.__path,path))
    def __call__(self,path):
        return Getapi('%s:%s' % (self.__path,path))
    def __str__(self):
        return self.__path  
    __repr__=__str__

print(Getapi().user('zhangsan').group('33').userinfo)

#执行原理是getattr递归(有参数的话执行call递归)281 

#使用枚举类

from enum import Enum
#自动赋值1到7

Week=Enum('Week',('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'))
for name,member in Week.__members__.items():
    print(name,'=>',member,',',member.value)

from enum import Enum,unique
#@unique用来检查重复
@unique
class sex(Enum):
    male=0
    female=1
    other=2

for name,member in sex.__members__.items():
    print(name,'=>',member,',',member.value)

print(sex.female)
print(sex(1))
print(sex.female.value)

#使用元类 type()函数可以查看一个类型或者变量的类型
from hello import Hello
h=Hello()
h.hello()
print(type(Hello))#<class 'type'>
print(type(h))#<class 'hello.Hello'>

#Hello是一个class类型就是type,是另一个实例类型是class Hello
#type函数可以创建新的类型
def fn(self,name='world'):
    print('hello, %s' % name)
Hello1=type('Hello1',(object,),dict(__init__=fn))#创建Hello1 class

h1=Hello1('list')

print(type(Hello))#<class 'type'>
print(type(h))#<class 'hello.Hello'>

#type函数第一个参数class的名称
#第二个参数继承的父类集合
#第三个方法名称与函数绑定

#python解释器遇到class类定义时,也是调用type()函数创建出class

#metaclass 元类,控制类的创建行为,类可以看成是元类创建的实例
#必须从type派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

#传入关键字参数metaclass,指示定制类     
class Mylist(list,metaclass=ListMetaclass):
    pass

#__new__方法的参数分别为
#第一个    当前准备创建的类的对象
#第二个 类的名字
#第三个 类继承集合,第四个类的方法集合

l=Mylist()
l.add(1)
print(l)

#object relational mapping (ORM)对象——关系映射,
#数据库中一个表对应一个类,一行对应一个对象
#父类Model和属性类型StringField、IntegerField是由ORM框架提供的
# class User(Model):
    # id=IntegerField('id')
    # name=StringField('username')
    # pw=StringField('password')

# u=User(id=12,name='lixiang',pw='1')#实例
# u.save()#保存

class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name
        
#进一步定义各种类型的Field

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
#接下来编写ModelMetaclass

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found Model %s' % name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s => %s' % (k, v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)    
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)
        
#基类model
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kv):
        super(Model,self).__init__(**kv)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
    
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,key,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id=IntegerField('id')
    name=StringField('username')
    pw=StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

















