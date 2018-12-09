#自定义异常类
class MyException(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return str(self.message)
try:
    a=11/1
    # 断言,如果条件不满足，则会报错且程序不再往下执行
    assert a>30
    if a==11:
        # 主动抛出异常 比如条件语句中不满足条件时 可以主动抛出异常后不再执行下去了
        raise MyException('sorry 我是一个自定义异常')
except Exception as e: # 如果try 代码块中出现了异常，会执行except中的代码，表示捕捉到了异常
    print(str(e))
# 如果try代码块中没有捕捉到异常，会执行else中的代码
else:
    print('no exception')
# 不管有没有发生异常，finally中的代码都会被执行，而且是最后执行
finally:
    print('end finaliy')
