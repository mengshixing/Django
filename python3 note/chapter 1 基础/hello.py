# 输入输出

name=input()

print('hello',name)

# 字符串加\转义  r'' 表示''内部的内容不转义

print('i\'m \"ok\"!')

# 空值None,常量大写

#除法 //地板除

print(10/3,10//3);

#字符串编码 unicode编码的默认  ord()函数获取字符的整数表示,chr()把编码转化为对应的字符

print (ord('A'))

print (chr(25991))

#字符串编码  b'' 表示byte编码  decode()方法可以将bytes变为str  len()字符的长度

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('中国'),len('中国'.encode('utf-8')))

#占位符 %d 整数  %f 小数 %s 字符串  %x 十六进制   %3d 表示占3个位宽   %03d 表示至少补齐3位  %.2f小数点保留2位

#字符串中的%可以用%%来表示  type()来获取变量类型

print('%3d' % 22,'%03d' % 22)

#练习：

#小明的成绩从72分提升到了85分,计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位

print(type((85-72)/72))

print('小明成绩提升了%.1f%%' % ((85-72)*100/72))


#有序集合list  len()长度 append()添加元素到最后  insert()插入指定位置

list1=['jack','lili','lucy']

print(len(list1),list1[0],list1[-1])

list1.append('lilei')

list1.insert(1,'hanmeimei')

print(list1)

#list 删除元素pop() 删除指定位置 默认最后一个

list1.pop();

list1[2]=['aa',123]

print(list1); print(list1[2])

#tuple 类似与list 一旦初始化 就不能再修改了 tuple只有1个元素时，为防止歧义需加,

tuple1=('jack','lili','lucy') 

tuple2=(1); tuple3=(1,)

print(tuple1,tuple2,tuple3)

#tuple 元素指向的元素是可以改变的

tuple4=('jack','lili','lucy',[123,'abc']); print(tuple4)

tuple4[3][1]='changed'; print(tuple4)

#退出



exit()
