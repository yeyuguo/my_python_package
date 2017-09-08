#coding:utf-8
# import httplib
import requests
import json
#just_send() pacakge
# import urllib
# import urllib2
# import random
# import cookielib
# import json
# import urlparse
# import sys
from wxpy import *
# import traceback
# from .log import errorMsg

__all__ = ['WX_wxpy']
'''
TODO: 微信换成后台登录的方式，扫码登录，会被阻塞
'''


# ip : 117.73.146.134
AppID_j = 'wxfa07a57d7110deac'
AppSecret_j = 'a44d0a55b51779fa0106201dbaadf02a'
access_token_j = 'xxxxx'

class WX_base():
    def __init__(self):
        self.AppID_j = 'wxfa07a57d7110deac'
        self.AppSecret_j = 'a44d0a55b51779fa0106201dbaadf02a'
        self.access_token_j = 'xxxxx'
        pass
    
    def get_token(self):
        url='https://api.weixin.qq.com/cgi-bin/token'
        values = {
            'grant_type':'client_credential',
            'appid' : self.AppID_j,
            'secret':self.AppSecret_j,
        }
        req = requests.post(url, params=values)  
        data = json.loads(req.text)
        return str(data["access_token"])


class WX_wxpy(WX_base):
    def __init__(self):
        '''
        基类使用：
        参考文章:http://www.cnblogs.com/Joans/archive/2012/11/09/2757368.html
         '''
        WX_base.__init__(self)
        print self.AppID_j # 测试是否连接上基类  
        
        self.login()
    def login(self):
        try:
            self.bot = Bot(console_qr = 1,login_callback=self.login_in_tip)
        except Exception,e:
            # print traceback.format_exc()
            logger.warning('微信登陆失败')
        else:
            self.myself = self.bot.self
        
    def send_msg(self,msg='测试测试'):
        try:
            self.bot.file_helper.send(msg.decode('utf-8'))
        except Exception,e:
            print u'WX_wxpy.send_msg error:',e
            self.bot.file_helper.send(msg.decode('utf-8'))
        finally:
            print u'发送结束'

    @classmethod
    def wx_logging(cls):
        '''
        这是 logging 的方式发送的消息;
        '''
        from wxpy import get_wechat_logger
        self.logger = get_wechat_logger()
        self.logger.warning('这是一条 WARNING 等级的日志，你收到了吗？'.decode('utf-8'))
        self.logger.warning('这是第二条 WARNING 等级的日志，你收到了吗？'.decode('utf-8'))
        self.logger.warning('这是第三条 WARNING 等级的日志，你收到了吗？'.decode('utf-8'))

    def login_in_tip(self):
        print u'叶:成功登陆 微信端'
        pass


def weixin(access_token='5ZnO1lhqQ-xZhn8E27ak5QILNsmewn66L1YCYjrojLKfqc1keXtAlrw5ESzhxad8aY5HRhgVX__v4CsbEXYJTYvQ6zXNie-TkpxwIyW7nDHQvwFTBPfQVn9d4vI9gKDMAOTgABADRW'):
    '''
    模拟发送消息
    '''
    access_token = get_token()
    if access_token is None:
        return
    conn = httplib.HTTPConnection("api.weixin.qq.com:80")#微信接口链接
    headers = {"Content-type":"application/json"} #application/x-www-form-urlencoded
    params = ({'touser' : AppID_j,#用户openid
        'template_id' : 'AtFuydv8k_15UGZuFntaBzJRCsHCkjNm1dcWD3A-11Y',#模板消息ID
        'url' : 'http://www.jb51.net',#跳转链接
        "topcolor" : "#667F00",#颜色
        "data" : {#模板内容
            "first" : {"value" : "尊敬的710.so : 您的网站http://www.jb51.net (192.168.1.1) 有异常访问", "color" : "#173177"},
            "keyword1" : {"value" : "访问时间 2015-04-05 15:30:59 访问IP 192.168.1.2", "color" : "#173177"},
            "keyword2" : {"value" : "访问链接 http://www.jb51.net", "color" : "#173177"},
            "remark" : {"value" : "访问频率 10/s", "color" : "#173177"}
        }
    })
    conn.request("POST", "/cgi-bin/message/template/send?access_token="+access_token, json.JSONEncoder().encode(params), headers)#推送消息请求
    response = conn.getresponse()
    data = response.read()#推送返回数据
    if response.status == 200:
        print 'success'
        print data
    else:
        print 'fail'

    pass

def just_send():
    '''
    模拟登陆 web 微信公众号后发送消息
    '''
    
    #构造登录数据
    data={'username':'2937487815@qq.com',   #用户名
        'pwd':'jc19911112', #加密后的密码
        'imgcode':'',
        'f':'json'
        }
    #Referer 很重要，不然会报错的
    header = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'),('Referer','https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=42111567')]
    #构造cookie 
    cj = cookielib.LWPCookieJar()
    cookie_suppot = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_suppot,urllib2.HTTPHandler)
    opener.addheaders = header
    urllib2.install_opener(opener)
    #登录
    request = urllib2.Request('https://mp.weixin.qq.com/',urllib.urlencode(data))
    conn=opener.open(request)
    # js = json.loads(conn.read())
    #获取令牌，可以从登录后的返回结果中获取，PS:因为这个字符串不是固定的，所以需要获取
    # token = dict(urlparse.parse_qsl(js['redirect_url']))['token']
    # print token
    #发送消息的URL
    url="https://mp.weixin.qq.com/cgi-bin/singlesend"
    url="https://mp.weixin.qq.com/cgi-bin/singlesend"
    #构造发送信息的数据，使用POST方法
    
    data1 = {
        'type':'1',
        'content':'这是要发送的数据',
        'tofakeid':'oGWFkweuwrAx4hwh9qrvwtU3N1Ps',  #接受消息的订阅人，可以从页面中获取
        # 'quickreplyid':'114647964', 
        'imgcode':'',
        'token': '1329521647',         #令牌
        'lang':'zh_CN',
        'random':random.random(),   #小于1的随机数
        'f':'json',
        'mask':'false',
        'ajax':'1',
        't':'ajax-response',
    }
    # data2 = {
    #     token:'1329521647',
    #     lang:'zh_CN',
    #     f:'json',
    #     ajax:1,
    #     random:random.random(),
    #     'mask':'false',
    #     tofakeid:'oGWFkweuwrAx4hwh9qrvwtU3N1Ps',
    #     imgcode:'',
    #     type:1,
    #     'content':'test',
    #     'appmsg':'',
    #     'quickreplyid':'114647964'
    # }
    #发送消息
    qe = urllib2.Request(url,urllib.urlencode(data1))
    res = opener.open(qe)
    pass




if __name__ == "__main__":
    # access_token = get_token()
    # weixin(access_token)

    # just_send()
    xx = WX_wxpy() 
    xx.send_msg('参数测试')
    pass