# author:gongnanxiong
# date:2018/12/3

import re
class Calculator():
    def __index__(self):
        pass

    def check(self,string):
        flag=True
        #左边括号和右边括号数量不对等；包含非数字，连续两个.都会被过滤掉
        if re.search('[a-zA-Z]]',string):
            flag=False
        elif re.search('\.\.',string):
            flag = False
        elif len(re.findall('\(',string))!=len(re.findall('\)',string)):
            flag = False
        else:pass
        return flag

    def format(self,string):
        #对+- -+ =* 等进行转换
        string=str(string).replace('+-','-')
        string=str(string).replace('-+','-')
        string=str(string).replace('--','+')
        string=str(string).replace('++','+')
        string=str(string).replace('+*','-')
        string=str(string).replace('+-','-')


