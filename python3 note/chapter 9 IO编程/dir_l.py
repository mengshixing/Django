#利用os模块编写一个能实现dir -l输出的程序。

#将st_mode获取的类型转换为dir -l第一个字符
def file_type(p):
    return {'040':'d','041':'d','0100':'-','020':'c','060':'b','010':'p','0140':'s'}[p]

#将st_mode获取的权限类型转换为rwx(读写执行)
def perm(p):    
    return {'0':'---','1':'--x','2':'-w-','3':'-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}[p]
    
    
#使用pwd和grp模块，根据os.stat(path).st_uid和st_gid，将uid和gid号转化成用户和所属的组，
#如果操作系统没有对应的用户和所属的组，返回uid和gid本身


        
#使用time模块转换时间，dir -l的时间默认是文件、目录等的修改时间，
#通过os.path.getmtime获取修改时间，然后和本地时间进行对比。
#os.path.getmtime和time.time()返回的是时间戳，两者可以进行加减运算，详情可以查官方文档关于time模块的说明

#Linux对于时间久远的文件或者目录等的输出是用年月日，这里定义如果修改时间在一年前的，显示年月日，否则显示年月时分
import os
import time
from os import path,stat


def modify_time(p):
    import time
    import os
    from os import path,stat
    
    mtime=os.path.getmtime(p)
    ltime=time.time()
    if abs(ltime-mtime)>float(31556926):
        return time.strftime('%b %d %Y',time.localtime(path.getmtime(p)))
    else:
        return time.strftime('%b %d %H:%M',time.localtime(path.getmtime(p)))




def dir_l(d):
    for l in os.listdir(d):#循环文件夹下所有子类
        fulldir=os.path.join(d,l)#完整路径
        #os.stat权限模块
        #print(os.stat(r'E:\123\Django\python3 note\chapter 8 错误，调试和测试'))
        #输出
        #(st_mode=16895, st_ino=5629499534246713, st_dev=521639, st_nlink=1, st_uid=0, st_gid=0,
        # st_size=4096, st_atime=1497944771, st_mtime=1497944771, st_ctime=1497856761)       
        
        #oct()函数转换8进制
        stmode=oct(stat(fulldir).st_mode)
        
        # print(os.stat(r'E:\123\Django\python3 note\chapter 8 错误，调试和测试')) 
        # print(oct(stat(r'E:\123\Django\python3 note\chapter 8 错误，调试和测试').st_mode)[-3:])
        # print(oct(stat(r'E:\123\Django\python3 note\chapter 8 错误，调试和测试').st_mode)[:-3])
        
        #获取dir -l第一个字符
        #去掉前两位0o(代表8进制),补0
        ftype1=file_type('0'+stmode[2:-3])

        #print(oct(stat(r'E:\123\Django\python3 note\chapter 8 错误，调试和测试').st_mode)[-3:])
        #输出'777'
        #map()遍历执行函数操作
        #join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。        

        # var_list = ['tom', 'david', 'john']
        # a = '###'
        # a.join(var_list) =  'tom###david###john'
        
        ftype2=''.join(map(perm,stmode[-3:])) #获取执行权限
        
        #str()字符串化函数
        fnum=str(stat(fulldir).st_nlink)
        
        #获取用户,组
    
        if os.name=='nt':
            #split(str="", num=string.count(str))方法语法：
            #str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
            user=os.popen('net user').readlines()[4].split()[1]
            group=os.popen('net user').readlines()[4].split()[0]
        else:
        
            import pwd,grp
            
            #pwd模块提供了一个unix密码数据库即/etc/passwd的操作接口，这个数据库包含本地机器用户帐户信息
            #pwd.getpwuid(uid)：返回对应uid的示例信息

            #grp模块提供了一个操作unix用户组即/etc/group数据库的接口
            #grp.getgrgid(gid)：返回对应gid的组信息

            stat_info=stat(fulldir)
            uid=stat_info.st_uid
            gid=stat_info.st_gid
            try:
                user=pwd.getpwuid(uid)[0]
                group=grp.getgrgid(gid)[0]
            except:
                user,group=str(uid),str(gid)
        
        mtime=modify_time(fulldir)
        
        #rjust() 返回一个原字符串右对齐,并使用空格(或指定字符)填充至长度 width 的新字符串
        print(ftype1+ftype2,fnum.rjust(5),user.rjust(5),group.rjust(5),mtime,l)
        #print(user[4])
        #print(time.time())
 
if __name__=='__main__':
    dir_l(r'E:\123\Django\python3 note')
