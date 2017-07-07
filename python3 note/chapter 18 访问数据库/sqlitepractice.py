# -*- coding: utf-8 -*-

import os, sqlite3,sys

# 当"print os.path.dirname(__file__)"所在脚本是以完整路径被运行的
# 那么将输出该脚本所在的完整路径，比如：
# Python d:/pythonSrc/test/test.py那么将输出 d:/pythonSrc/test

# 当"print os.path.dirname(__file__)"所在脚本是以相对路径被运行的
# 那么将输出空目录，比如：
# python test.py那么将输出空字符串
# print(os.path.dirname(__file__))

# sys.exit()

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    #' 返回指定分数区间的名字，按分数从低到高排序 '
    

    conn= sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select name from user where score >= ? and score <= ? order by score asc',(low, high))

    data=cursor.fetchall()

    cursor.close()
    conn.commit()
    conn.close()
    
    
    print(data)#[('Bart',), ('Lisa',)]
    
    dataset=[]
    
    for i in data:
        dataset.append(i[0])
        
    print(dataset)#['Bart', 'Lisa']
    
    print(x[0] for x in data)#<generator object get_score_in.<locals>.<genexpr> at 0x0000021A8AD568E0>
    
    print([x[0] for x in data])#['Bart', 'Lisa']
    return [x[0] for x in data]
get_score_in(60,90)