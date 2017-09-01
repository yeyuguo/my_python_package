#coding:utf-8
from . import *

@app_B.route('/test')
def main():
    # return 'app_B.main()'
    return jsonify({'a':'b'})

