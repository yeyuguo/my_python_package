#coding:utf-8
__all__ = ['qq_send_mail']


'''
测试已经成功的邮件
从 QQ 邮箱 发送到其他的邮箱
'''
import smtplib
import traceback
from email.mime.text import MIMEText
from .log import errorMsg


_user = "346243440@qq.com"
_pwd  = "llheofyodztymrbhegb"
_to   = "xxx@xxx.com.cn"
_pwd  = "llheofodztmrbheb"
_to   = "yeyuguo@goldwind.com.cn"


def qq_send_mail(user=_user,pwd=_pwd,to_user=_to,subject="这是主题名称",msg_text="这是邮件的内容"):
    # msg = MIMEText(msg_text,'plain','utf-8')
    msg = MIMEText(msg_text)
    msg["Subject"] = subject
    msg["From"]    = user
    msg["To"]      = to_user

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(user, pwd)
        s.sendmail(user, to_user, msg.as_string())
        s.quit()
        print "Success send mail!"
    except smtplib.SMTPException,e:
        print "Falied send mail,%s "%e
        errorMsg(e,'邮件发送失败【邮件主题是：%s】'%(subject))


# _user = "346243440@qq.com"
# _pwd  = "llheofyodztymrbhegb"
# _to   = "xxx@xxx.com.cn"
# msg = MIMEText("这是邮件的内容")
# msg["Subject"] = "这是主题名称"
# msg["From"]    = _user
# msg["To"]      = _to
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     s.login(_user, _pwd)
#     s.sendmail(_user, _to, msg.as_string())
#     s.quit()
#     print "Success!"
# except smtplib.SMTPException,e:
#     print "Falied,%s"%e 

if __name__ == '__main__':
    qq_send_mail()