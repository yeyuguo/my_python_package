#coding:utf-8
print __name__
print __package__
from mongo.index import *
from common.log import errorMsg

# try:  
#     1/0  
# except Exception,e:  
#     print e  
#     errorMsg(e,'测试错误 ing')
mongo = Mongo()
client = mongo.client

print client.address
print [doc for doc in client.testDB.hehe.find()]

# if __name__ == '__main__':
#     Mongo.replicaSet()
#     pass