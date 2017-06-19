#4 pdberr 启动pdb 程序单步方式运行
s='22'
m=int(s)
print(m*4)

#以参数-m pdb启动后 
# l查看代码 n下一行 p 变量名 查看变量值 q结束调试

#5 pdb.set_trace(),设置断点

import pdb

s='22'
m=int(s)

pdb.set_trace()#运行到此处暂停进入pdb环境 p查看变量 c继续

print(m*4)

#6 靠谱的IDE