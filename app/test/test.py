import os
import re


print __file__
# print os.path.dirname(__file__)
print os.path.dirname(os.path.dirname(__file__))
path = os.path.dirname(os.path.dirname(__file__))
router = path.rindex('.')

# @app.route('/<path:path>')
def main(path):
    #  动态引包：https://blog.csdn.net/hhczy1003/article/details/76662184 
    # re.findall('/(.)', '/a/b/c') # ['a','b', 'c']
    routeList = re.findall('/(.)',path)
    result = False
    try:
        router = '.'.join(routeList)
        module = importlib.import_module(router)
        
    except Exception as e:
        pass
    else:
        pass

