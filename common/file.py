#coding:utf-8
import os

class File():
    def __init__(self,file,path=None,model='r'):
        if path is None:
            path = ''
        path_file = os.path.join(path,file)
        try:
            self.f = open(path_file,model);
        except Exception,e:
            pass
        finally:
            pass
            self.f.close()

    def read(self):
        # TODO
        pass
    def write(self,data):
        # TODO
        pass




