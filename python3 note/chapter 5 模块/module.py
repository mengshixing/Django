#在python中一个py文件可以称为一个模块,模块名即文件名
#python按目录组织模块的方法称为包package,包目录下有__init__.py文件
#__init__.py文件也是一个模块,模块名即包名,系统自带sys模块

import test

print(1)
print(test.hello())

print(test.__doc__)
#作用域__author__ __name__属于特殊变量,可以直接引用
#_xx和__xx类似的变量是private,不应该被直接引用

def _private1(name):
	print('hello %s' % name)
def _private2(name):
	print('hi %s' % name)
def greeting(name):
	if len(name)>3:
		_private2(name)
	else:
		_private2(name)
		
greeting('222222')

#这是一种代码封装抽象的原则,即外部不会直接引用的都定义成private

#安装第三方的包通过pip,pip install Pillow

#找不到引入的库会报stdin错误

import sys
print(sys.path)

from PIL import Image

im=Image.open('1.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('2.jpg','JPEG')