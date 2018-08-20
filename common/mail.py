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
from .types import chENG




def qq_send_mail( to_user='xxx@xxx.com.cn', subject="这是主题名称",msg_text="这是邮件的内容", sender='346243440@qq.com', pwd='llheofyodztymrbhegb' ):

    # msg = MIMEText(msg_text,'plain','utf-8')
    msg = MIMEText(msg_text)
    msg["Subject"] = subject
    msg["From"]    = sender
    msg["To"]      = to_user

    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(sender, pwd)
        s.sendmail(sender, to_user, msg.as_string())
        s.quit()
        print "Success send mail!"
    except smtplib.SMTPException,e:
        print "Falied send mail,%s "%e
        errorMsg(e,'邮件发送失败【邮件主题是：%s】'%(subject))

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def outlook_send_mail(to_user, subject='头信息:前端获取接口异常', msg_text='后端速解决',sender=None,pwd=None):
    # https://stackoverflow.com/questions/30314618/having-trouble-with-sending-an-email-through-smtp-python
    # 天蝎默认值
    if sender is None: 
        sender = ''
    if pwd is None: 
        pwd = ''
    # print to_user, subject, msg_text,sender, pwd
    company = '公司地址' # 类似的 mail.qq.com => 这里填 qq.com
    to_user = to_user + "@" + company
    username = sender + "@" + company
    password = pwd
   
    # print '====', to_user, subject, msg_text,sender, pwd
    msg_text = msg_text.encode("utf-8")
    # subject = subject.encode("utf-8")


    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_user
    msg['Subject'] = subject
    
    # !msg_text 需要是字符类型
    # print 'msg_text:',type(msg_text) 
    msg.attach(MIMEText(msg_text))

    try:
        print 'sending mail to ' + to_user + 'header: ' + subject

        # mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer = smtplib.SMTP('mail.'+company, 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, to_user, msg.as_string())
        mailServer.close()

    except Exception as e:
        errorMsg(e,msg=subject+msg_text)
        return False
    else:
        return True
    


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
    # qq_send_mail()
    outlook_send_mail('jiangchen', '前端获取接口异常', '以后都这样发给你')