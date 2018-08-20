#coding:utf-8
from . import app_test
from common import log
from .__init__ import *
import importlib
import pdb
from common.decorator import toJson
__cur_module = 'app.test'

@app_test.route('/<path:path>',methods=['GET','POST'])
@toJson
def main(path):
    # re.findall('/(.)', '/a/b/c') # ['a','b', 'c']
    # routeList = re.findall('/(.)',path)
    # router = '.'.join(routeList)
    if path is not None:
        router = path.replace('/','.')
    else:
        return '路由不能为空'
    params = request.values.to_dict()
    result = ''
    try:
        # !处理 引包异常问题
        # 动态引包：https://blog.csdn.net/hhczy1003/article/details/76662184 
        # 动态引入相对路径 https://blog.csdn.net/xie_0723/article/details/78004649
        module = importlib.import_module("."+router, package=__cur_module)
    except Exception as e:
        result = u'%s 动态引包 执行报错'%(router)
        log.errorMsg(e,msg = result )
    else:
        # !处理 函数执行异常
        try:
            result =  module.main(**params)
        except Exception as func_err:
            # todo 把参数设置在错误信息里
            result = u'%s - main() 函数执行错误'%(router)
            log.errorMsg(func_err, msg=result)
    finally:
        return result


from flask import render_template
@app_test.route('/api')
def api():
    return render_template('test_api.html')