#coding:utf-8
print __package__
print __name__

from pymongo import *
from common.log import logging,errorMsg
# from common.config import Config
from common.config import getConfig
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

__all__ =['Mongo']

# cfg = Config()
host = getConfig("database",'dbhost')
port = getConfig("database",'dbport')
replSet = getConfig("database",'replSet')
user = getConfig("database",'dbuser')
password = getConfig("database",'dbpassword')

print '%s:%s:%s'%(host,port,replSet)


mongo_url =  "mongodb://%s:%s@%s" % (quote_plus(user), quote_plus(password), host)

class Mongo():
    pass
    def __init__(self,host=host,port=port,db=None,collection=None):
        self.client = self.__conn__(host,port)
        self.db = db
        self.collection = collection
    
    def __collect__(self,db=None,collection='test'):
        if db is None and self.db is not None:
            db = self.db
        collection = self.client[db][collection]
        return collection
    
    def __db__(self,db):
        if self.db is not None:
            db = self.db
        db = self.client[db]
        return db
    
    def __conn__(self,host='127.0.0.1',port=27017,preferences='nearest'):

        try:
            # 参数配置 http://api.mongodb.com/python/current/api/pymongo/errors.html#pymongo.errors.AutoReconnect
            '''
            primary 连接失败,自动连接 Secondary
            '''
            # client = MongoClient('%s:%s'%(host,port),replicaSet=replSet,readPreference=preferences)
            client = MongoClient(mongo_url,
                replicaSet=replSet,
                readPreference=preferences,
                localThresholdMS=35 # 使用负载均衡,连接多个server共同读取
                ) 
        except Exception,e:
            msg = u'连接数据库失败'
            errorMsg(e,msg)
        else:
            msg = '连接上数据库 %s'%(client.address)
            logging.info(msg)
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
                msg = u'建立 replSet 失败'
                logging.error('%s,详细错误:(%s)'%(msg,e))
                client.close()
                return False
            else:
                msg = u'成功建立 replSet : %s, 配置参数为: %s'%(result,config)
                logging.info('%s'%(msg));
                client.close()
                return True
            
    
    def main(self):
        pass
    


