
#Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

import sqlite3

#链接到数据库文件,不存在的话会创建一个新文件
conn=sqlite3.connect('user.db')

#连接到数据库后，需要打开游标，称之为Cursor，
#通过Cursor执行SQL语句，然后，获得执行结果。

cursor=conn.cursor()#创建一个cursor

#创建表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id,name) values (\'1\',\'jack\')')

# 通过rowcount获得插入的行数:
print(cursor.rowcount)

cursor.close()#关闭游标

#提交
conn.commit()
conn.close()

# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。
# 结果集是一个list，每个元素都是一个tuple，对应一行记录。

# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，
# 有几个?占位符就必须对应几个参数