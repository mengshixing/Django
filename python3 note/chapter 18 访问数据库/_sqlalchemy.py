# 把一个表的内容用Python的数据结构表示出来的话，
# 可以用一个list表示多行，list的每一个元素是tuple
# ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上

from sqlalchemy import Column,String,create_engine,ForeignKey

from sqlalchemy.orm import sessionmaker,relationship

from sqlalchemy.ext.declarative import declarative_base

#创建对象基类
Base=declarative_base()

#继承基类
class User(Base):

    __tablename__='user'
    
    
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    
    school_id=Column(String(20),ForeignKey('school.id'))
    
#初始化连接  
engine=create_engine('mysql+pymysql://root:123456@localhost:3306/test')

engine.execute('create table if not exists school(id varchar(20) primary key, name varchar(20))')
engine.execute('drop table if exists user')
engine.execute('create table if not exists user(id varchar(20) primary key, name varchar(20) ,school_id varchar(20))')
#创建DBSession类型
DBsession=sessionmaker(bind=engine)

class School(Base):

    __tablename__='school'
    
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    
    users=relationship('User')
    
    
    
#初始化一个session对象
session=DBsession()

# 创建新User对象:
new_User=User(id='11',name='hado',school_id='2')
new_User2=User(id='22',name='patuo',school_id='2')

new_school=School(id='2',name='yizhong')
# 添加到session:
session.add(new_User2)
#session.add(new_school)
session.add(new_User)
#session.commit()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
qre=session.query(User).filter(User.id=='11').one()


print(qre,qre.name)#<__main__.User object at 0x7f1f5906e0f0> kaka

qre2=session.query(School).filter(School.id=='2').one()


print(qre2,qre2.name)#<__main__.School object at 0x7fae61742cf8> yizhong
print(qre2.users)#[<__main__.User object at 0x7fae622e94e0>, <__main__.User object at 0x7fae6282e240>]

session.close()




















