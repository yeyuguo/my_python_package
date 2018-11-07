# coding:utf-8
from . import *
from .A.index import app_A
from .mail.index import app_mail
from .test.index import app_test   # API 测试模块

from flask_cache import Cache


app = Flask(__name__, template_folder='templates')

# cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


'''
目的激活 应用(app) 的上下文（全局环境）
区别于 flask.g ：flask.g 是每个请求的上下文；
'''
ctx = app.app_context()
ctx.push()

# 测试使用上下文
# print 'current_app:', dir(current_app)
current_app.a = 'aaaaa'
current_app.cache = cache
print 'current_app-a:', current_app.a
print 'current_app.cache:', current_app.cache


# 允许跨域
from flask_cors import CORS
CORS(app, supports_credentials=True)

app.register_blueprint(app_A, url_prefix='/A')
app.register_blueprint(app_mail, url_prefix='/mail')
app.register_blueprint(app_test, url_prefix='/test')  # API 测试模块


@app.route('/')
def main():
    return 'index.main()'


from flask import render_template


@app.route('/api')
def api():
    # return 'index.main()'
    return render_template('api.html')
