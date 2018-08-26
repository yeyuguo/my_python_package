#coding:utf-8
import logging,time,os
import traceback
from email.mime.text import MIMEText
import smtplib



__all__ = ["logging","errorMsg"]

def set_log_fileTime():
    pass
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    # print otherStyleTime
    return otherStyleTime

# set_log_fileTime()

import os
path = os.path.dirname(__file__) 
logsPath = path + '/../logs'
if os.path.exists(logsPath)  is False:
    os.makedirs(logsPath)

error_mongo_file = os.path.join(os.path.split(os.path.realpath(__file__))[0] + '../logs/mongo/error_%s.log'%set_log_fileTime())

'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
设置写入文件的 最低警报级别+
'''
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='logs/%s.log'%(set_log_fileTime()),
    # filemode='a'
)

def errorMsg(e=None,msg=None):
    # tractback:  http://blog.csdn.net/handsomekang/article/details/9373035
    errInfo = '(%s),详细错误:%s'%(msg,e)
    logging.error('%s --- 错误代码 --- %s'%(errInfo,traceback.format_exc()))
    # traceback.print_exc(file=open(error_mongo_file,'w+'))



# 参考文章  http://blog.csdn.net/akin912/article/details/45243171
# class OptmizedMemoryHandler(logging.handlers.MemoryHandler):  
#     def __init__(self, capacity, mail_subject, mail_host, mail_from, mail_to):  
#         """ 
#         日志邮件 发送服务
#             capacity: flush memory 
#             mail_subject: warning mail subject 
#             mail_host: the email host used 
#             mail_from: address send from; str 
#             mail_to: address send to; multi-addresses splitted by ';' 
 
#         """  
#         logging.handlers.MemoryHandler.__init__(self, capacity, 
#             flushLevel = logging.ERROR,  
#             target = None)  
#         self.mail_subject = mail_subject  
#         self.mail_host = mail_host  
#         self.mail_from = mail_from  
#         self.mail_to = mail_to  
  
#     def flush(self):  
#         """if flushed send mail 
#         """  
#         if self.buffer != [] and len(self.buffer) >= self.capacity:  
#             content = ''  
#             for record in self.buffer:  
#                 message = record.getMessage()  
#                 content += record.levelname + " occurred at " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(record.created)) + "  : " + message + '\n'  
#             self.send_warning_mail(self.mail_subject, content,self.mail_host, self.mail_from, self.mail_to)  
#             self.buffer = []  
  
#     def send_warning_mail(self, subject, content, host, from_addr, to_addr):  
#         """send mail 
#         """  
#         msg = MIMEText(content)
#         msg['Subject'] = subject  
#         try:  
#             smtp = smtplib.SMTP()  
#             smtp.connect(host)  
#             smtp.sendmail(from_addr, to_addr, msg.as_string())  
#             smtp.close()  
#         except:
#             # traceback.format_exc()   # 转成字符串
#             traceback.print_exc(file=open(error_mongo_file,'w+'))   # 会写入文件



'''
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

msg = u'自定义错误信息'
logging.error('%s,详细错误:(%s)'%(msg,e))
'''





