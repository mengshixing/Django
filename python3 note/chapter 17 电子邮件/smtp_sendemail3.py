# SMTP  发送附件 及图片等


from email.mime.text import MIMEText
import sys
from email.utils import parseaddr,formataddr
from email.header import Header
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from_addr=input('from email')

from_pw=input('from pw')

to_addr=input('to email')

smtp_server='smtp.163.com'


def _format_addr(s):
    name,addr=parseaddr(s)#('梦<222@qq.com>')解析为:梦 222@qq.com
    #print(Header(name, 'utf-8').encode())编码为 =?utf-8?b?5qKm?=
    #print(formataddr((Header(name, 'utf-8').encode(),addr)))
    #输出 =?utf-8?b?5qKm?= <222@qq.com>
    return formataddr((Header(name, 'utf-8').encode(),addr))

# _format_addr('梦<222@qq.com>')
# sys.exit()


# 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造
# 一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
# 再继续往里面加上表示附件的MIMEBase对象即可：


#定义邮件对象

# 同时支持HTML和Plain格式
# 如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，
# 但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？
# 办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，
# 就可以自动降级查看纯文本邮件。
# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
msg=MIMEMultipart('alternative')

#邮件正文是MIMEText:
text=MIMEText('<html><body><h1>python test html</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p><img src="cid:0">' +
    '</body></html>','html','utf-8')

#在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，
#给它们依次编号，然后引用不同的cid:x即可。

msg.attach(MIMEText('hello', 'plain', 'utf-8')) #添加文本 不支持html时候会加载文本
msg.attach(text)#添加正文html

msg['From']=_format_addr('发件人XXX<%s>' % from_addr)
msg['To']=_format_addr('收件人XXX<%s>' % to_addr)
msg['Subject']=Header('test sencend 第二次测试','utf-8').encode()

with open('email.md', 'rb') as f:
    # 设置附件的MIME和文件名:
    mime=MIMEBase('','',filename='email.md')
    #添加头信息
    mime.add_header('Content-Disposition','attachment',filename='email.md')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    
    mime.set_payload(f.read()) # 把附件的内容读进来
    encoders.encode_base64(mime)#用Base64编码
    
    msg.attach(mime)
with open('222.png', 'rb') as f:
    # 设置附件的MIME和文件名:
    mime=MIMEBase('image','png',filename='222.png')
    #添加头信息
    mime.add_header('Content-Disposition','attachment',filename='222.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    
    mime.set_payload(f.read()) # 把附件的内容读进来
    encoders.encode_base64(mime)#用Base64编码
    
    msg.attach(mime)    
import smtplib

#使用SSL加密端口163的邮箱默认465
server=smtplib.SMTP_SSL(smtp_server,465)#默认端口25,SSH默认465

#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)

#login()方法用来登录SMTP服务器，
server.login(from_addr,from_pw)

server.sendmail(from_addr,[to_addr],msg.as_string())

server.quit()




