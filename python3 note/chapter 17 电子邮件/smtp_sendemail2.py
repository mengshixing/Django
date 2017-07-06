# SMTP SSL 加密发送 html正文


#使用smtplib.SMTP不通，只能使用smtplib.SMTP_SSL，
from email.mime.text import MIMEText

# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
# 发送html5的话第二个参数'html'
msg=MIMEText('<html><body><h1>python test html</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')


from_addr=input('from email')

from_pw=input('from pw')

to_addr=input('to email')

smtp_server='smtp.163.com'

import sys
from email.utils import parseaddr,formataddr
from email.header import Header
from email import encoders

def _format_addr(s):
    name,addr=parseaddr(s)#('梦<222@qq.com>')解析为:梦 222@qq.com
    #print(Header(name, 'utf-8').encode())编码为 =?utf-8?b?5qKm?=
    #print(formataddr((Header(name, 'utf-8').encode(),addr)))
    #输出 =?utf-8?b?5qKm?= <222@qq.com>
    return formataddr((Header(name, 'utf-8').encode(),addr))

# _format_addr('梦<222@qq.com>')
# sys.exit()

import smtplib

#使用SSL加密端口163的邮箱默认465
server=smtplib.SMTP_SSL(smtp_server,465)#默认端口25,SSH默认465

#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)




#login()方法用来登录SMTP服务器，
server.login(from_addr,from_pw)


msg['From']=_format_addr('发件人XXX<%s>' % from_addr)
msg['To']=_format_addr('收件人XXX<%s>' % to_addr)
msg['Subject']=Header('test sencend 第二次测试','utf-8').encode()

server.sendmail(from_addr,[to_addr],msg.as_string())

server.quit()


# test sencend 第二次测试

    # 发件人：
    # 发件人XXX<**@163.com>
    # 收件人：
    # 收件人XXX<***@126.com>
    # +
    # 时   间：
    # 2017年07月06日 11:22 (星期四)

# 精简信息k
# x
# 维达制造商，100%进口原木浆材质面巾纸，无增白剂无荧光剂，安全又健康！   独家发售>>

# python is best language

