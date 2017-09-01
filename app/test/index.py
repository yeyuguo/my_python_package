#coding:utf-8
from . import app_test



@app_test.route('/test')
def main():
    return 'app_test.main()'

