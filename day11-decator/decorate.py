# author:gongnanxiong
# date:2018/11/27

'''
装饰函数一定要放在被装饰函数的上面，不然会报错，找不到
'''
import time

def func_decorate(f):
    def inner():
        start=time.time()
        time.sleep(2)
        f()
        end=time.time()
        print("spend %s's" % (end-start))
    return inner


@func_decorate # func_1=func_decorate(func_1)
def func_1():
    print('func_1')

# func_1=func_decorate(func_1)
func_1()





