# -*- coding: utf-8 -*-

# centos6.5安装mysql:http://www.centoscn.com/mysql/2014/1211/4290.html

# 1 rpm -qa | grep mysql　　// 这个命令就会查看该操作系统上是否已经安装了mysql数据库

# 2 rpm -e mysql　　// 普通删除模式
  # rpm -e --nodeps mysql　　// 强力删除模式，如果使用上面命令删除时，
                        # 提示有依赖的其它文件，则用该命令可以对其进行强力删除
                        
# 3 yum install -y mysql-server mysql mysql-deve 安装mysql数据库所需要的软件以及其它附属的一些软件
# 4 service mysqld start
    # /usr/bin/mysqladmin -u root password 123456 //配置密码
    # /usr/bin/mysqladmin -u root -h xiaoluo password 'new-password'

    # chkconfig --list | grep mysqld命令来查看mysql服务是不是开机自动启动
    # chkconfig mysqld on 命令来将其设置成开机启动
    # 1/etc/my.cnf 这是mysql的主配置文件
    # 2./var/lib/mysql   mysql数据库的数据库文件存放位置
    # 3./var/log mysql数据库的日志输出存放位置
    
    
    
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动
# 来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，
# 但是安装的时候需要给pip命令加上参数--allow-external：
# $ pip install mysql-connector-python --allow-external mysql-connector-python

# 如果上面的命令安装失败，可以试试另一个驱动：
# $ pip install mysql-connector

#都不行的话换一个库pip install pymysql或者pip3 install pymysql

#在window10 64测试  pip install mysql-connector可以正常安装

#import mysql.connector
import pymysql

conn=pymysql.Connect(user='root',password='123456',database='test',charset='utf8')

cursor=conn.cursor()

cursor.execute('create table user (id varchar(25) primary key,name varchar(25))')

cursor.execute('insert into user (id,name) values (\'2\',\'tom\')')
print(cursor.rowcount)

#执行INSERT等操作后要调用commit()提交事务
conn.commit()#提交

cursor.close()#关闭

cursor=conn.cursor()

#MySQL的SQL占位符是%s。
cursor.execute('select * from user where id = %s',('2',))

print(cursor.fetchall())

cursor.close()

conn.close()

