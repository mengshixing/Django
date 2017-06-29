#datetime是Python处理日期和时间的标准库。

from datetime import datetime#从datetime模块引入datetime类
print(datetime.now()) #2017-06-22 12:03:05.981096
print(type(datetime.now())) #<class 'datetime.datetime'>

#获取指定日期和时间,用参数构造一个datetime

dt=datetime(12,2,22,22,22,22)
print(dt)#0012-02-22 22:22:22

#datetime互相转换timestamp
#timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00 = 1970-1-1 08:00:00 UTC+8:00

now=datetime(2013,2,2,2,2,2)
print(now.timestamp())#1359741722.0
print(datetime.fromtimestamp(now.timestamp()))#2013-02-02 02:02:02

#上面都是本地时区
print(datetime.utcfromtimestamp(now.timestamp()))#2013-02-02 02:02:02

#str转换为datetime
strday=datetime.strptime('2002-12-2 12:2:00','%Y-%m-%d %H:%M:%S')
print(strday)
print(type(strday)) #此时是没有时区的

#datetime转换为str
print(datetime.now().strftime('%A,%B, %H:%M:%S'))

#datetime加减,使用timedelta
from datetime import timedelta
print(datetime.now()+timedelta(hours=10))
print(datetime.now()-timedelta(days=10))
print(datetime.now()+timedelta(hours=10,days=99))

#本地时间转换为UTC时间,引用datetime的tzinfo属性
from datetime import timezone
utc_8=timezone(timedelta(hours=8))#创建+8区
#replace(tzinfo=当前时区)即可转换标准时区
print(datetime.now().replace(tzinfo=utc_8))

#时区转换,我们可以先通过utcnow()拿到UTC时间,进而进行转换
print(datetime.utcnow())
#print(datetime.utcnow().replace(tzinfo=timezone.utc)需要先设置时区,当前设为0
print(datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(utc_8))
#设置基准时间之后
print(datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=9))))

#练习：2015-1-21 9:01:30，以及一个时区信息如UTC+5:00,转换timestamp
def test(s1,s2):
    # s1='2015-1-21 9:01:30'
    # s2='UTC+5:00'
    test1=datetime.strptime(s1,'%Y-%m-%d %H:%M:%S')
    print(test1)

    import re
    szone=re.match(r'^UTC([+-])(\d*):(\d*)',s2)
    print(szone.groups())
    print(szone.group(1))

    if szone.group(1)=='+':
        s3=int(szone.group(2))
        s4='minutes='+szone.group(3)
    else:
        s3=int('-'+szone.group(2))
        s4='minutes='+szone.group(3)
    print(s3,s4)
    print(re.match(r'\S+?00',s4))
    if(re.match(r'00',s4)):
        print(test1+timedelta(hours=s3))
    else:
        print(test1+timedelta(hours=s3))
        
    print(test1.replace(tzinfo=timezone(timedelta(hours=s3))).timestamp())
    return test1.replace(tzinfo=timezone(timedelta(hours=s3))).timestamp()

t1=test('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2=test('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2


