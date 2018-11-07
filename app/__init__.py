# coding:utf-8
print 'module app.__init__'
'''
该文件引入 API 内使用到 flask 公共模块包
'''

from flask import Flask, g, make_response, Blueprint, jsonify, request, current_app

# print 'current_app:', current_app
