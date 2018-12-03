# author:gongnanxiong
# date:2018/12/3

# import re
# class Calculator():
#     def __index__(self):
#         pass
#
#     def check(self,string):
#         flag=True
#         #左边括号和右边括号数量不对等；包含非数字，连续两个.都会被过滤掉
#         if re.search('[a-zA-Z]]',string):
#             flag=False
#         elif re.search('\.\.',string):
#             flag = False
#         elif len(re.findall('\(',string))!=len(re.findall('\)',string)):
#             flag = False
#         else:pass
#         return flag
#
#     def format(self,string):
#         #对+- -+ =* 等进行转换
#         string=str(string).replace('+-','-')
#         string=str(string).replace('-+','-')
#         string=str(string).replace('--','+')
#         string=str(string).replace('++','+')
#         string=str(string).replace('+*','-')
#         string=str(string).replace('+-','-')



import re

#这里是检查是否有字母函数
def check(s):
    #定义一个变量True，判断是否有字母，有字母退出，没字母返回True
    flag = True
    if re.findall('[a-zA-Z]', s):
        print('表达式不规范!')
        flag = False
    return flag

#格式化字符串函数  将一些'--''+-''*+''-+'等不规则的转换为规则的下面很多步骤都要用
def format_string(string):
    string = string.replace('--', '+')
    string = string.replace('-+', '_')
    string = string.replace('++', '+')
    string = string.replace('+-', '-')
    string = string.replace('*+', '*')
    string = string.replace('/+', '/')
    string = string.replace('+*', '*')
    string = string.replace('+/', '/')
    #返回格式完的表达式
    return string

#这里是乘除函数
def mul_div(expression):
    #定义正则表达式可以匹配到类似'x*y' / 'x/y'
    mul_div_regular = '\d+\.?\d*[*/]\d+\.?\d*'
    #得到匹配到的第一个符合的表达式字符段
    ret = re.search(mul_div_regular, expression)
    #这里判断是否找到乘除表达式了，如果匹配为空，直接返回这个表达式进行加减运算就可以了
    if not ret:
        return expression
    #如果不为空就说明匹配到了，就开始运算
    else:
        #获得这个字符串
        ret1 = ret.group()
        #判断是否有/
        if len(ret1.split('/')) > 1:
            x, y = ret1.split('/')
            result = float(x) / float(y)
        #判断是否有*
        if len(ret1.split('*')) > 1:
            x, y = ret1.split('*')
            result = float(x) * float(y)
        #没有的话直接pass就行了，就会剩加减到下个函数运行
        else:
            pass
        #得到的浮点型要强制转换字符串
        result1 = str(result)
        #这里是用字符串结果替换刚找到的这个表达式块例如（x*y）
        re_expr = re.sub(mul_div_regular, result1, expression, count=1)
        #上面是运算了一小块，这里是不断调用乘除运算并且每次调用都会格式化表达式，直到表达式没有乘除符号了就返回这个括号内表达式的结果了
        fina_expr = mul_div(format_string(re_expr))
        return fina_expr

#这是加减函数
def add_sub(expression):
    #定义正则表达式
    add_sub_regular = '\-?\d+\.?\d*[\+\-]\d+\.?\d*'
    #下面跟上面没有大区别，上面能看懂，这里也能看懂
    ret = re.search(add_sub_regular, expression)
    if not ret:
        return expression
    else:
        ret1 = ret.group()
        if len(ret1.split('+')) > 1:
            x, y = ret1.split('+')
            result = float(x)+float(y)
        else:
            x, y = ret1.split('-')
            result = float(x) - float(y)
        result1 = str(result)
        re_expr = re.sub(add_sub_regular, result1, expression, count=1)
        #不断调用加减函数并格式化字符串
        fina_expr = add_sub(format_string(re_expr))
        return fina_expr


if __name__ == '__main__':
    source = input('请输入表达式(退出q):')
    #检查是否有字母
    if check(source):
        #去空格去一次就够了
        source = source.replace(' ', '')
        #格式化 具体看上面format_string()函数
        source = format_string(source)
        print('表达式:', source)

        #进入while循环，只要有括号，就一直在这个循环里运行
        while source.count('(') > 0:
            #寻找第一个最内层括号以字符串的格式获取
            strs = re.search('\([^()]+\)', source).group()
            #运行第一个括号内的乘除得到返回值
            replace_str = mul_div(strs)
            #运行此括号内的加减并得到返回值
            replace_str = add_sub(replace_str)
            #得到字符串是结果和括号，去掉括号并在整体表达式中用结果替换原先的内容 到这里相当于运算了一个括号里的表达式并用结果替代了原先的位置
            source = format_string(source.replace(strs, replace_str[1:-1]))
            #然后上去继续判断是否还有括号，有括号就继续，直到剩下没有括号的表达式运行else
        else:
            #没有括号的表达式直接先乘除运算后加减运算
            replace_str = mul_div(source)
            replace_str = add_sub(replace_str)
            #输出结果
            print(replace_str)




