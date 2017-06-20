#dict 类,要实现效果如下:
# >>> d = Dict(a=1, b=2)
# >>> d['a']
# 1
# >>> d.a
# 1


class Mydict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):
		print('getattr1 %s' % key)
		try:
			return self[key]
		except KeyError:
			raise AttributeError('dict has no attribute %s' % key)
	def __setattr__(self,key,value):
		print('setattr1 %s' % key)
		self[key]=value

#test		
# d=Mydict(**{'name':'Tom','age':21})
# print(d.name)
# print(d['name'])

# e=Mydict(name='Tom',age=22)
# print(e.age)
# print(e['age'])