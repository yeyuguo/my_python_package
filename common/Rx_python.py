#coding:utf-8
import rx
from rx import Observable, Observer
import gevent
import time
from weixin import WX_wxpy
import pdb 

wx = None

# def ttt():
#     global wx
#     time.sleep(2)
#     wx = 'yesssss'
def push_five_strings(observer):
    wx = 'xxxxx'
    observer.on_next(wx)


class PrintObserver(Observer):
    # global wx
    def on_next(self, x):
        # time.sleep(2)
        print 'wx:',wx
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("completed")
def console():
    print wx
aa = Observable.create(push_five_strings)
pdb.set_trace()
aa.subscribe(PrintObserver())
aa.subscribe(wx.send_msg)

def bbb():
    if wx is not None:
        wx.send_msg('yes')
        pass

# Observable.from_(wx)

# gevent.joinall([gevent.spawn(ttt),gevent.spawn(ttt)])