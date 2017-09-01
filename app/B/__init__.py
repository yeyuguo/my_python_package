#coding:utf-8
# print 'module app.B.__init__'
from .. import *  # 引入所有的 app.__init__ 里的所有模块
app_B = Blueprint('B',__name__)