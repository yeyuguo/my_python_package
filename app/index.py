#coding:utf-8
from . import *
from .A.index import app_A
from .B.index import app_B
from .test.index import app_test   # API 测试模块

app = Flask(__name__,template_folder='templates')

# 允许跨域
from flask_cors import CORS
CORS(app, supports_credentials=True)

app.register_blueprint(app_A,url_prefix='/A')
app.register_blueprint(app_B,url_prefix='/B')
app.register_blueprint(app_test,url_prefix='/test') # API 测试模块  


@app.route('/')
def main():
    return 'index.main()'


from flask import render_template
@app.route('/api')
def api():
    # return 'index.main()'
    return render_template('api.html')