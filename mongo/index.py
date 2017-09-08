#coding:utf-8
print __package__
print __name__

import gevent
from pymongo import *
from common.log import logging,errorMsg
from common.mail import qq_send_mail
from common.weixin import WX_wxpy
from common.config import getConfig
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

__all__ =['Mongo']

import pdb # 调试代码 TODO 需要删除的

# 读取配置文件
host = getConfig("database",'dbhost')
port = getConfig("database",'dbport')
replSet = getConfig("database",'replSet')
replSet_num = getConfig("database",'replSet_num')
user = getConfig("database",'dbuser')
password = getConfig("database",'dbpassword')

print '%s:%s:%s'%(host,port,replSet)

# 异步登陆微信端
wx_global = None
node_warning = ''

def weixin_tmp():
    global wx_global
    wx_global = WX_wxpy()
    # wx_global.send_msg('hahahah')

def tttt():
    while wx_global is None:
        gevent.sleep(0)
        return 
    print u'yes，终于异步过了'
    wx_global.send_msg(node_warning)
    
    


class Mongo():
    pass
    def __init__(self,host=host,port=port,db=None,collection=None):
        self.client = self.__conn__(host,port)
        nodeLength = len(self.client.nodes)
        print self.client.nodes
        print nodeLength
        # 异步发送邮件 警报
        gevent.joinall([gevent.spawn(self.nodes_tip(nodeLength))])
        # for t in _t:
        #     print t
        print u'测试会不会阻塞'
        # # 测试节点连接 一个都没有
        # try:
        #     self.client.test.test.find_one()
        # except Exception,e:
        #     msg = 'mongodb 操作 document 检测，连接不上'
        #     print msg
        #     errorMsg(e,msg)
        # 无任何集群节点，退出数据库
        if nodeLength == 0:
            return None

        if db is not None:
            self.db = self.__db__(db)
        else:
            self.db = None
        if db is not None and collection is not None:
            self.collection = self.__collect__(db,collection)
        else:
            self.collection = None

    
    def __collect__(self,db=None,collection='test'):
        '''
        获取 mongodb collection
        '''
        if db is None and self.db is not None:
            db = self.db
        collection = self.client[db][collection]
        return collection
    
    def __db__(self,db):
        '''
        获取 mongodb database 
        '''
        if self.db is not None:
            db = self.db
        db = self.client[db]
        return db
    
    def __conn__(self,host='localhost',port=27017,preferences='nearest'):
        '''
        获取 mongodb 连接的 client
        '''
        try:
            # 参数配置 http://api.mongodb.com/python/current/api/pymongo/errors.html#pymongo.errors.AutoReconnect
            '''
            primary 连接失败,自动连接 Secondary
            '''
            
            mongo_url =  "mongodb://%s:%s@%s:%s,%s:%s" % (quote_plus(user), quote_plus(password), host, port,host,int(port)+1)
            print 'mongo_url:',mongo_url
            # client = MongoClient('%s:%s'%(host,port),replicaSet=replSet,readPreference=preferences)
            client = MongoClient(mongo_url,
                replicaSet=replSet,
                readPreference=preferences,
                localThresholdMS=35 # 使用负载均衡,连接多个server共同读取
                )
            print '===>',client.nodes 
        except Exception,e:
            msg = '连接数据库失败'
            errorMsg(e,msg)
        else:
            # msg = '连接上数据库 %s'%(client.address)
            # logging.info(msg)
            return client

    def __call__(self):
        pass

    @staticmethod
    def replicaSet(host='127.0.0.1',port=27017):
        '''
        建立容灾备份数据库，端口自增加 1
        '''
        _id = 0  #默认其实 ID 值
        config = {'_id': replSet, 'members': [
            {'_id': int(_id), 'host': '%s:%s'%(host,port)},
            {'_id': int(_id)+1, 'host': '%s:%s'%(host,int(port)+1)}
        ]}
        print config
        try:
            client = MongoClient('%s:%s'%(host,port))
            result = client.admin.command("replSetInitiate", config)
        except Exception,e:
            print e;
            logging.error(e)
            client.close()
            return False
        else:
            if not result.has_key('ok'):
                msg = '建立 replSet 失败'
                logging.error('%s,详细错误:(%s)'%(msg,e))
                client.close()
                return False
            else:
                msg = '成功建立 replSet : %s, 配置参数为: %s'%(result,config)
                logging.info('%s'%(msg));
                client.close()
                return True
    def nodes_tip(self,node_num=2):
        '''
        集群异常，邮件提醒
        '''
        # TODO 微信发消息被阻塞了发不了
        global node_warning
        
        # if wx is None:
        #     wx = WX_wxpy()

        if node_num == 1:
            '''
            只有一个运行的节点
            TODO 邮件 发送，提醒集群只有一个或不存在集群了
            '''
            node_warning = '该 "%s" 集群只剩下一个,目前正在运行的 mongodb server 节点有:,%s'%(replSet,[p[1] for p in self.client.nodes])
            logging.warning(node_warning)
            qq_send_mail(subject="mongodb 集群 backup 剩余一个节点预警",msg_text=node_warning,to_user="346243440@qq.com")
            
        elif node_num == 0 :
            '''
            没有任何运行的节点
            TODO 微信 发送，提醒集群没有节点运行
            '''
            print u'测试发送邮件'
            node_warning = '该 "%s" 集群没有运行的集群,目前正在运行的 mongodb server 节点有:%s'%(replSet,self.client.nodes)
            logging.error(node_warning)
            # gevent.joinall([gevent.spawn(qq_send_mail,subject="mongodb 集群 backup 无节点预警",msg_text=node_warning,to_user="346243440@qq.com")])
            
            qq_send_mail(subject="mongodb 集群 backup 无节点预警",msg_text=node_warning,to_user="346243440@qq.com")
            # gevent.joinall([gevent.spawn(qq_send_mail,subject="mongodb 集群 backup 无节点预警",msg_text=node_warning,to_user="346243440@qq.com"),gevent.spawn(weixin_tmp)])
            # pdb.set_trace()
            # if wx_global is None:
            #     gevent.sleep(0)
            # else:
            #     print u'正在发送消息'
            #     wx_global.send_msg(node_warning)
            # if wx_global is None:
            #     while 
            # else:
            #     print u'正在发送消息'
            #     wx_global.send_msg(node_warning)
            # pass
            
            
        # print msg.decode('unicode')
    def main(self):
        pass
    


