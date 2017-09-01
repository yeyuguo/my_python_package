#coding:utf-8
from . import app_A

@app_A.route('/test')
def main():
    return 'app_A.main()'




