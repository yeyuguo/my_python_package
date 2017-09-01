#coding:utf-8
import sys
from app.index import app

from common.config import getConfig

server_host = getConfig("server",'server_host')
server_port = getConfig("server",'server_port')

print 'server is %s:%s'%(server_host,server_port)

def runServer(debug=True,port=80):
    print 'port is %s:'%port

    if debug:
        app.run(debug=True,host=server_host,port=port)
    else:
        from tornado.wsgi import WSGIContainer
        from tornado.httpserver import HTTPServer
        from tornado.ioloop import IOLoop
        import tornado.web
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(port)
        IOLoop.instance().start()


if __name__ == '__main__':
    #runServer(debug=False,port=sys.argv[1])
    debug = False
    port = server_port
    if len(sys.argv)>1:
        debug = sys.argv[1]
    elif len(sys.argv)>2:
        debug = sys.argv[1]
        port = sys.argv[2]
    runServer(debug=debug,port=port)