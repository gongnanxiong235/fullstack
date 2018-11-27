'''
变量的作用域:
1.局部变量无法改变全局变量的值, 如果想要改变全局变量的值需要在局部变量前加上global 先声明
2.局部变量如果和全局变量重名不能直接用，需要先声明
3.变量都是从内到外找，内层找不到再去外层找，同样内层无法改变外层的值，需要声明关键字global,nonlocal(嵌套函数)
'''

age=18
def func1():
    age=73
    def func2():
        print ( age )  # 调用age，本级没有向上查找
    return func2  # 函数func1（）返回函数func2（）的名字func2，而不是func2（）这个函数
a=func1 ()  # 此时的a就等于函数func1（）返回的func2（）的函数名func2
print ( a )
a ()  # 那a再加上括号就等同于func2（）这个函数



# def scope_test():
#     spam="test spam"
#     def do_local():
#         spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
#     def do_nonlocal():
#         nonlocal  spam        #使用外层的spam变量
#         spam = "nonlocal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     do_local()
#     print("After local assignmane:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:",spam)
#     do_global()
#     print("After global assignment:",spam)
#
# scope_test()
# print("In global scope:",spam)


def f():
    print("ok")
a=f
a()
