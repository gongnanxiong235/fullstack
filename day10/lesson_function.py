# author:gongnanxiong
# date:2018/11/22
import time
def logger(contents):
    current_time=time.strftime('%Y-%m-%d %X')
    with open('log.txt','a',encoding='utf-8') as file_log:
        file_log.write('%s:%s\n' % (current_time,contents))

logger('lohgger_1')
logger('lohgger_2')
logger('lohgger_3')
logger('lohgger_4')