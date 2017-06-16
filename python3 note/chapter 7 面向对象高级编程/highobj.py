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
	#__getitem__()方法传入参数可能有多种
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
    
        
for n in Fibseries():
    print(n)

print(Fibseries()[3])
print(Fibseries()[13])






















