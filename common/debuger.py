#coding:utf-8

'''
可以解决依赖包问题
1.以最顶层目录运行脚本  python -m xxx.xxx.xxx 

命令行进入debuger
2. ipython test.py  --pdb

类似 JS 的 debugger     python内部自带
import pdb
3. pdb.set_trace()



'''

import pdb # 调试代码 TODO 需要删除的
import sys

class ExceptionHook:
# 参考文章 ： https://www.zhihu.com/question/21572891
    instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            from IPython.core import ultratb
            self.instance = ultratb.FormattedTB(mode='Plain',
                 color_scheme='Linux', call_pdb=1)
        return self.instance(*args, **kwargs)
sys.excepthook = ExceptionHook()