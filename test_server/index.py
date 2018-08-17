# coding:utf-8
from flask import Flask
import importlib, os, re
app = Flask(__name__)


@app.route('/<path:path>')
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
        module = importlib.import_module(router)
        return module.main()
    except Exception as e:
        pass
    else:
        return '报错了'

@app.route('/main')
def main2():
    return 'index.main()'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
