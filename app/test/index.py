#coding:utf-8
from . import app_test
from .__init__ import *




@app_test.route('/test')
def main():
    return 'app_test.main()'

