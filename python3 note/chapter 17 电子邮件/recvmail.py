# http://www.cnblogs.com/fujinliang/archive/2012/06/30/2570764.html
# 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。
# 收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。

# Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

# 注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，
# 和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。
# 要把POP3收取的文本变成可以阅读的邮件，还需要用email模块
# 提供的各种类来解析原始文本，变成可阅读的邮件对象。

# 所以，收取邮件分两步：
# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象。

#通过POP3下载邮件
import poplib

#设置接受邮件地址,密码pop服务器地址
#toaddr=input('recv email addr')
#topw=input('recv email pw')
topop='pop.126.com'

toaddr='programmer_msx@126.com'
topw='199142'

server=poplib.POP3(topop)#初始化连接pop服务器

server.set_debuglevel(1)#日志级别1

print(server.getwelcome().decode('utf-8'))
#打印POP欢迎文字
#+OK Welcome to coremail Mail Pop3 Server (126coms[75c606d72bf436dfbce6e08e565f41f7s])

server.user(toaddr)
server.pass_(topw)#认证用户/密码

# stat()返回邮件数量和占用空间:服务器返回：邮件总数和总字节数。
print(server.stat())#(380, 51824449) 380封邮件，约50M

# list()返回所有邮件的编号:
# LIST(LIST命令针对pop3邮箱会首先返回+ok 邮件总数 邮件总大小，
# 但对于pop邮箱则只返回+ok状态字符，因此最好还是通过STAT来判断邮件总数)
print(server.list())
resp, mails, octets = server.list()

#获取最新一份邮件

index=len(mails)
#print(server.retr(index)) 最新一封邮件
#RETR  <邮件的序号> 从服务器中获得一个邮件。
resp, lines, octets = server.retr(index)


#DELE服务器将邮件标记为删除，当执行QUIT命令时才真正删除

# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')

from email.parser import Parser

msg=Parser().parsestr(msg_content)#把邮件内容解析为Message对象：

#print(msg)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()


#解析邮件

from email.header import decode_header
from email.utils import parseaddr


#msg=Parser().parsestr(msg_content)把邮件内容解析为Message对象：


#邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
def decode_str(str):

    # decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，
    # 所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。    
    value,charset=decode_header(str)[0]    
    if charset:
        value=value.decode(charset)    
    return value
    
    
# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset=msg.get_charset()
    #print(charset)  
    if charset is None:
        content_type=msg.get('Content-Type', '').lower()
        #print(content_type) 
        
        # Python find() 方法检测字符串中是否包含子字符串 str 
        # 如果包含子字符串返回开始的索引值，否则返回-1。
        pos=content_type.find('charset=')
        
        #如果存在charset=字符的话,截取到末尾并移出空格
        if pos>=0:
            charset=content_type[pos+8:].strip()
            
    return charset
#print(guess_charset(msg))   

#但是这个Message对象本身可能是一个MIMEMultipart对象，
#即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
#递归打印Message层次

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def print_into(msg,indent=0):#解析msg

    if indent==0:#第一层
        #获取'From','To','Subject'的值
        for header in ['From','To','Subject']:
            value=msg.get(header,'')
            
            #如果值存在
            if value:
            
                #如果Subject内容值存在解码
                if header=='Subject':
                    value=decode_str(value)
                    
                #对于'From','To',解析出名字和地址
                else:
                    hdr,addr=parseaddr(value)
                    name=decode_str(hdr)
                    value=u'%s<%s>' % (name,addr)
                    
                    
                # u'string'  表示 已经是 unicode 编码的 'string' 字符串
                # 而 unicode('string') 是 即将要把 'string' 转化为 unicode 编码
                # (但在执行这条语句之前，还不一定是unicode编码）

            print('%s%s: %s' % ('  ' * indent, header, value))

            # From: 发件人XXX<xxxx@163.com>
            # To: 收件人XXX<xxx@126.com>
            # Subject: test sencend 第二次测试
    
    #如果是多层
    if(msg.is_multipart()):     
        parts = msg.get_payload()#解析msg
        
		# Python中有一个内置函数enumerate会将数组或列表组成一个索引序列。
		# 使我们再获取索引和索引内容的时候更加方便快捷
        for n, part in enumerate(parts):
		
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_into(part, indent + 1) #递归调用
		
		# part 0
		# --------------------
		# part 1
		# --------------------
		# part 2
		# --------------------
		# part 3
		# --------------------
     
	#最后一层
    else:
        content_type = msg.get_content_type()
		
		#如果是文件内容
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)#获取内容编码
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
		#附件
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))      
    # part 0
	# --------------------
	  # Text: hello...
	# part 1
	# --------------------
	  # Text: <html><body><h1>python test html</h1><p>send by <a href="http://www.python.org">Python</a>...</p><img src="cid:0"></body></html>...
	# part 2
	# --------------------
	  # Attachment: /
	# part 3
	# --------------------
	  # Attachment: image/png
		
	
print_into(msg)
















