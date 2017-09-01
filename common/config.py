#coding:utf-8
import os
import ConfigParser

__all__ = ['getConfig']

class Config():
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        path = os.path.split(os.path.realpath(__file__))[0] + '/../cfg.conf'
        self.config.read(path)
        pass

    def getConfig(self,section, key):
        # config = ConfigParser.ConfigParser()
        # os.path.split(os.path.realpath(__file__))[0] 是 该文件所在路径
        # path = os.path.split(os.path.realpath(__file__))[0] + '/../cfg.conf'
        # path = os.path.split(os.path.realpath(__file__))[0] + '/../cfg.conf'
        return self.config.get(section, key)


getConfig = Config().getConfig