#coding:utf-8
from . import app_mail
from .__init__ import *

import importlib
@app_mail.route('/<path:path>')
def main(path):
    #  动态引包：https://blog.csdn.net/hhczy1003/article/details/76662184 
    # re.findall('/(.)', '/a/b/c') # ['a','b', 'c']
    print 'path:',path
    # routeList = re.findall('/(.)',path)
    # router = '.'.join(routeList)
    if path is not None:
        router = path.replace('/','.')
    else:
        return '路由不能为空'

    try:
        # 动态引入相对路径 https://blog.csdn.net/xie_0723/article/details/78004649
        module = importlib.import_module("."+router, package='app.mail')
        print dir(module)
        return module.main()
    except Exception as e:
        pass
    else:
        return '报错了'



from flask import render_template
@app_mail.route('/api')
def api():
    return render_template('mail_api.html')