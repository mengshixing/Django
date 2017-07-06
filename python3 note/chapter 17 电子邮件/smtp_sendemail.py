
# SMTP是发送邮件的协议，Python内置对SMTP的支持，
# 可以发送纯文本邮件、HTML邮件以及带附件的邮件。

# Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，smtplib负责发送邮件。


#使用smtplib.SMTP不通，只能使用smtplib.SMTP_SSL，
from email.mime.text import MIMEText

# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
msg=MIMEText('python is best language','plain','utf-8')


from_addr=input('from email')

from_pw=input('from pw')

to_addr=input('to email')
import smtplib

server=smtplib.SMTP(smtp_server,25)#默认端口25,SSH默认465

#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)

#login()方法用来登录SMTP服务器，
server.login(from_addr,from_pw)

# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
# 邮件正文是一个str，as_string()把MIMEText对象变成str。

#报错
# Traceback (most recent call last):
  # File "smtp_sendemail.py", line 41, in <module>
    # server.sendmail(from_addr,[to_addr],msg.as_string())
  # File "C:\Users\ben\AppData\Local\Programs\Python\Python35\lib\smtplib.py", line 883, in sendmail
    # raise SMTPDataError(code, resp)
# smtplib.SMTPDataError: (554, b'DT:SPM 163 smtp5,D9GowAC3HtCdpV1Z+VC2AA--.1469S2 1499309469,
# please see http://mail.163.com/help/help_spam_16.htm?ip=111.160.189.62&hostid=smtp5&time=1499309469')

#添加msg配置,错误消失
#分别配置了发件人地址,收件人地址,邮件主题
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']='test'

server.sendmail(from_addr,[to_addr],msg.as_string())


server.quit()












