#coding:utf-8


import json
from .log import errorMsg

def toJson(func):
    def wrapper(*args, **kwargs):
        status = 0
        error = None
        code = 200
        dataset = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            pass
            status = 0
            error = e
            code = 500
            errorMsg(e, msg='输出结果转json报错')
        else:
            status = 1
            dataset = result 
        finally:
            _result = {
                "status":status,
                "code":code,
            }
            if dataset is not None:
                _result['dataset'] = dataset
            else:
                _result['error'] = error
            return json.dumps(_result)
    return wrapper
