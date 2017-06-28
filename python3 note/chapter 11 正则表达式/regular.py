
#正则表达式

# 精准匹配:
# \d匹配一个数字
# \w匹配一个字母或数字
# \s匹配一个空格（也包括Tab等空白符）
# .可以匹配任意字符

# *表示0或多个
# +至少一个
# ?0或一个
# {n}n个字符
# {n,m}n至m个字符

# \d{3}\s+\d{3,8}解读

# \d{3}3个数字
# \s+至少一个空格
# \d{3,8}3到8个数字
# 匹配区号

import re
r1=r'\d{3}\s+\d{3,8}'
print(re.match(r1,'010  90090'))
if(re.match(r1,'010  90090')):
    print('OK')


#[]表示范围
# [0-9a-zA-Z\_] 匹配一个字母/数字或者下划线
# [0-9a-zA-Z\_]+ 匹配一个字母/数字或者下划线或者更多组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]*字母/下划线开头,后面0或多个字符组成的字符串,即python变量
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}后面字符0至19位

# ^匹配开头 $匹配结束
# py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了

phone_nub=input()
if(re.match(r'^\d{3}-\d{3,8}$',phone_nub)):#匹配序号
    print('OK')
else:
    print('failed')
    
#切分字符串
print('a b   c'.split(' '))#['a', 'b', '', '', 'c']
print(re.split(r'\s','a b   c'))#['a', 'b', '', '', 'c']
#匹配一个或者多个空格
print(re.split(r'\s+','a b   c'))#['a', 'b', 'c']
#匹配空格或者, 
print(re.split(r'[\s\,]+','a b   c,d'))#['a', 'b', 'c', 'd']
#匹配空格或者,或者;
print(re.split(r'[\s\,\;]+','a ;b   c,d'))#['a', 'b', 'c', 'd']
    
#分组
m=re.match(r'^(\d{3})-(\d{3,8})$','010-8881228')
print(m.group(0))#010-8881228获取第一个匹配项
print(m.group(1))#010获取匹配项第一部分
print(m.group(2))#8881228获取匹配项第二部分
print(m.groups())
#分组时间
t="2:22:22"  
time=re.match(r'^([0-1][0-9]|[0-9]|2[0-4]):([0-5][0-9]|[0-9]):([0-5][0-9]|[0-9])$',t)
print(time.groups())
print(time.group(1))    
print(time.group(2))   
print(time.group(3))  
    
#贪婪匹配,正则默认贪婪匹配

print(re.match(r'^(\d+)(0*)$','122200').groups())#('122200', '')
#上面是贪婪的,加+之后采用非贪婪匹配（也就是尽可能少匹配）
print(re.match(r'^(\d+?)(0*)$','122200').groups())#('1222', '00')

#预编译 鉴于一个正则表达式可能多次使用,可以预编译
re_phone=re.compile(r'^(\d{3})-(\d{3,8})$')  
  
print(re_phone.match('000-1111').groups())

#练习:请尝试写一个验证Email地址的正则表达式,并提取出带名字的Email
re_email=re.compile(r'^([0-9a-zA-Z][0-9a-zA-Z\_]*)@([a-zA-Z]+).([a-zA-Z]+)$')
    
print(re_email.match('shixi@gmail.com').groups())
    