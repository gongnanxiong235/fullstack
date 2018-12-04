# author:gongnanxiong
# date:2018/12/3


'''
模块之间的调用：
1.如果调用模块中有import其他的模块，这样除了在pycharm中执行外都会报错
pycharm 不报错是因为pycharm自动在sys.path 中把项目添加到了执行路径
比如在liunx中执行 是不会去自动添加的，所以找不到此路径就会报错


'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import lesson_configParseer
def add(*args):
    return sum(args)

print('HELLO',sys.path)
hello=lesson_configParseer.ConfigUtil()
# hello.add(**{'DATABASE':{'url':'url','password':'123456'}})
print(hello)
print(hello.read_config_database('url'))
print(hello.read_config_database('password'))

