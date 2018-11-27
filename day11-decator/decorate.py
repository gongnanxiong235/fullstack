# author:gongnanxiong
# date:2018/11/27

'''
被装饰的函数没有参数
装饰函数一定要放在被装饰函数的上面，不然会报错，找不到
'''
import time
#
# def func_decorate(f):
#     def inner():
#         start=time.time()
#         time.sleep(2)
#         f()
#         end=time.time()
#         print("spend %s's" % (end-start))
#     return inner
#
#
# @func_decorate # func_1=func_decorate(func_1)
# def func_1():
#     print('func_1')
#
# # func_1=func_decorate(func_1)
# func_1()

'''
被装饰的函数带参数
'''

# def deco(f):
#     def inner(x,y):
#         start=time.time ()
#         time.sleep(1)
#         f(x,y)
#         end=time.time()
#         print("spend %s's" % (end-start))
#     return inner
#
# @deco
# def fun_test(x,y):
#     print(x+y)
#
# fun_test(2,3)

'''
装饰函数带参数：应用场景为有些调用方法的地方不是一定要加装饰的
'''
def hello(flag='false',logger='false'):
    def deco(f):
        def inner(x,y):
            start=time.time ()
            time.sleep(1)
            f(x,y)
            end=time.time()
            if flag=='true':
                print("spend %s's" % (end-start))
            if logger=='true':
                print("hello logger")
        return inner
    return deco

@hello('true','true')
def fun_test(x,y):
    print(x+y)

fun_test(2,3)




