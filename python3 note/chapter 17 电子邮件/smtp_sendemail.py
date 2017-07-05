
# SMTP是发送邮件的协议，Python内置对SMTP的支持，
# 可以发送纯文本邮件、HTML邮件以及带附件的邮件。

# Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，smtplib负责发送邮件。

from email.mime.text import MIMEText

# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
msg=MIMEText('PY is best language','plain','utf-8')