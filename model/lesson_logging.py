# author:gongnanxiong
# date:2018/11/30
import logging
import sys
import os
from model import logger

'''
format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
'''
log_address=''
if sys.platform.startswith('win'):
    log_address='d\\hello_log.txt'
else:
    log_address='/Users/gongnanxiong/log.txt'

'''
文件输出和屏幕输出只能二选一
'''
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s-->%(filename)s-->lineno:%(lineno)s-->%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename=log_address,
#                     filemode='a')
# logging.debug("hello")
# logging.debug("hello1")
# logging.info('info')
# logging.warning('warong')
# logging.error('erro')
# logging.critical('critical')

'''
既可以文件输出也可以屏幕输出
'''
#
# loger=logging.getLogger()
# loger.setLevel(logging.DEBUG)
# fh=logging.FileHandler(log_address)
#
# sh=logging.StreamHandler()
#
#
# format=logging.Formatter('%(asctime)s-->%(filename)s-->lineno:%(lineno)s-->%(message)s')
#
# fh.setFormatter(format)
# sh.setFormatter(format)
#
# loger.addHandler(fh)
# loger.addHandler(sh)

# def log_stream_init(path):
#     loger = logging.getLogger()
#     loger.setLevel(logging.DEBUG)
#     fh = logging.FileHandler(log_address)
#     sh = logging.StreamHandler()
#     format = logging.Formatter('%(asctime)s-->%(filename)s-->lineno:%(lineno)s-->%(message)s')
#     fh.setFormatter(format)
#     sh.setFormatter(format)
#     loger.addHandler(fh)
#     loger.addHandler(sh)
#     return loger
#
# def setlog_stream_debug(message,path=log_address):
#     log_stream_init(path).debug(message)
#
# def setlog_stream_info(message,path=log_address):
#     log_stream_init(path).info(message)
#
# def setlog_stream_warong(message,path=log_address):
#     log_stream_init(path).warning(message)
#
# def setlog_stream_erro(message,path=log_address):
#     log_stream_init(path).error(message)
#
# def setlog_stream_critical(message,path=log_address):
#     log_stream_init(path).critical(message)

x=logger.logger(log_path='/Users/gongnanxiong/')
x.debug('hello')



