#coding:utf-8
from . import app_A
from .__init__ import *

@app_A.route('/test')
def main():
    return 'app_A.main()'




