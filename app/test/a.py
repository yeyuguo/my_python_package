# coding:utf-8
'''
@host = http://127.0.0.1:8080/
@content_obj = application/json
@content_str = application/x-www-form-urlencoded


GET http://127.0.0.1:8080/test/a HTTP/1.1 
Content-Type: application/json

{
    b:'hehe'
}

'''

# 使用全局变量
from .. import current_app
# print current_app.a

cache = current_app.cache


@cache.cached(timeout=50)
def main(b=None):
    print 'b:', b
    return ' test b, ---%s' % b
