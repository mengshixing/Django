#查询测试

import sqlite3

conn=sqlite3.connect('user.db')

cursor=conn.cursor()



# 使用Cursor对象执行select语句时，通过fetchall()可以拿到结果集。
# 结果集是一个list，每个元素都是一个tuple，对应一行记录。

# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?
# 占位符就必须对应几个参数cursor.execute('select * from user where name=?', ('abc'))

cursor.execute('select * from user')

dataset1=cursor.fetchall()

cursor.execute('select * from user where id=?',(1,))#(1,)tuple

dataset2=cursor.fetchall()
print(dataset1)
print(dataset2)
# [('1', 'jack')]
# [('1', 'jack')]
cursor.close()
conn.commit()

conn.close()