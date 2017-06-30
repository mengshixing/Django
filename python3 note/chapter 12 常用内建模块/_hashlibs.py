#摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
#目的是为了发现原始数据是否被人篡改过。

import hashlib
md5=hashlib.md5()

md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())#d26a53750bc40b38b65a520292f69306
print(md5.digest())#b'\xd2jSu\x0b\xc4\x0b8\xb6ZR\x02\x92\xf6\x93\x06'

# hash.new([arg])
# 创建指定加密模式的hash对象

# hash.update(arg)
# 更新哈希对象以字符串参数。如果同一个hash对象重复调用该方法，

# m.update(a); m.update(b) 等价于 m.update(a+b)

# hash.digest()
# 返回摘要，作为二进制数据字符串值。

# hash.hexdigest()
# 返回摘要，作为十六进制数据字符串值

# hash.copy()
# 复制

#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1=hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())#b752d34ce353e2916e943dc92501021c8f6bca8c

#练习1:根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

if __name__=='__main__':
    calc_md5('123456')#b752d34ce353e2916e943dc92501021c8f6bca8c

#实际使用中当然大都是加盐的

#练习2：根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db=dict()

def register(un,pw):
    if un in db.keys():
        print('already exist')
    else:
        md5=hashlib.md5()
        md5.update((un+pw+'salt').encode('utf-8'))
        db[un]=md5.hexdigest()

def login(un,pw):
    md5=hashlib.md5()
    md5.update((un+pw+'salt').encode('utf-8'))
    if db[un]==md5.hexdigest():
        print('login success')
    else:
        print('login fail')
        
if __name__=='__main__':
    register('a','2')
    login('a','2')
















