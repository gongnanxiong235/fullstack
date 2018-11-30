# author:gongnanxiong
# date:2018/11/28
'''
用生成器生成一个斐波那契数列0,1,1,2,3,5
'''
#普通方法生成
# def fibo(max):
#     n,before,after=0,0,1
#     while n<max:
#         print(before)
#         before,after=after,before+after
#         n+=1
#
# fibo(10)

'''
生成器的两种方法：
1.(a**3 for i in range(10))
2.yield  替代了普通方法的return
'''
#生成器
def fibo(max):
    n,before,after=0,0,1
    while n<max:
        yield before
        before,after=after,before+after
        # temp=before
        # before=after
        # after=temp+after
        n+=1
for i in fibo(10):
    print(i)

# import time
#sum([i for i in xrange(10000000000)])  --后果是直接卡死，太占用内存了
#print(sum(i for i in range(100000000)))  --用生成器 大大提高性能


'''
yield 的send方法
1.大致功能和next()一样，但是send方法可以传一个值给yield接收
2.send(None)=next()
3.迭代第一个元素必须要用next（）或者send（None）
'''

def test_yield_send():
    count=yield 1
    print('count:',count)
    count=yield 2
    print('count:', count)
    yield 3

gen=test_yield_send()  # 生成一个生成器对象
next(gen) # 取出生成器里面的第一个数据 到yield 1 结束
gen.send('hello') # 从yield 1 开始  这时候count==hello 往下走遇到yield 2 停止
gen.send('hello1') #从yield 2 开始 这时候count==hello2 往下走 直到遇到yield 3


'''利用yield send 实现伪并发'''

def person(name):
    while 1:
        number=yield
        print("第%s个包子被%s吃了" % (number,name))

def factory():
    person1=person('zhangsan')
    person2=person('lisi')
    person1.send(None)
    person2.send(None)
    for i in range(10):
        print("开始做包子了")
        person1.send(i+1)
        person2.send(i+1)

factory()

'''
迭代器
Iterable:可迭代的对象:list tuple dict set gennerrator string.可迭代的对象都有next() 和iter(） 方法
Iterator:迭代器对象:可迭代的对象.Iter 后生成的对象
可以用for 循环的都是可迭代对象，内部先转换成一个迭代器对象，然后通过next()方法一个个的取出来的，同时捕捉StopIter...异常
'''

from collections import Iterable,Iterator #Iterable:可迭代的对象,Iterator:迭代器对象
list_a=[1,2]
print(isinstance(list_a,list))#True
print(isinstance(list_a,Iterable))#True
print(isinstance(list_a,Iterator))#Flase
print(isinstance(list_a.__iter__(),Iterator))#True

print(isinstance((1,2),Iterable))#True
print(isinstance(set([1,2]),Iterable))#True
print(isinstance(person('hello'),Iterable))#True


'''
练习:一行代码搞定找到文件中最长的行
'''
max((len(line.strip()),for line in open('hello.txt',r,encoding='utf-8')))

