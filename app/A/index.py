#coding:utf-8
from . import app_A
from .__init__ import *

@app_A.route('/test')
def main():
    return 'app_A.main()'



from flask import render_template
@app_A.route('/api')
def api():
    return render_template('A_api.html')