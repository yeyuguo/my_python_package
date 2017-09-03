#coding:utf-8
import httplib
import requests
import json

AppID = 'wxab65d728d0827e49'
AppSecret = 'e1dacc8d02291b23c6ada3d4c634482a'
access_token = 'xxxxx'
 
def get_token():
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {
        'corpid' : 'your corpid' ,
        'corpsecret':'your corpsecret',
    }
    req = requests.post(url, params=values)  
    data = json.loads(req.text)
    return data["access_token"]

def weixin(access_token='xxx'):
    conn = httplib.HTTPConnection("api.weixin.qq.com:80")#微信接口链接
    headers = {"Content-type":"application/json"} #application/x-www-form-urlencoded
    params = ({'touser' : "oEGZ4johnKOtayJbnEVeuaZr6zQ0",#用户openid
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

if __name__ == "__main__":
    weixin()