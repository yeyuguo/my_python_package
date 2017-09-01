#coding:utf-8
import email
import os
import email.mime.multipart
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


from_addr = '346243440@qq.com'
password = 'llheofyodztymrbhegb'  # 第三方客户端需要用到的 授权码
to_addr = 'xxx@xxx.com.cn'

smtp_server = 'smtp.qq.com'
msg = MIMEText('hahaha','plain','utf-8')
msg['From'] = 'come from QQ account'
msg['To'] = '!'.join(to_addr)
msg['Subject'] = Header('test email for use','utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()