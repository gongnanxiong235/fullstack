import threading
import time

'''
多线程：
1.由于python的解释器Cpython 有一把大锁（GIL）导致，python使用多线程只能使用一个CPU，且同一时刻只能支持一个线程工作
2.python在处理IO密集型（阻塞,睡眠）的时候，用多线程可以提高效率，以为一个线程在阻塞的时候另一个线程可以抢占CPU资源处理另外的事情
3.python在处理计算密集型的时候，用多线程无法提高效率，因为几个线程用同一个CPU 且是轮换着工作，不但无法提高效率，且有可能比单线程慢，因为切换线程也需要时间
'''
import datetime,time,threading
# def foo():
#     print( 'foo1' )
#     print ( 'foo2' )
#     print ( 'foo3' )
#     print ( 'foo4' )
#     print ( 'foo5' )
#     print ( 'foo6' )
#     #time.sleep(1)
#     print ( 'foo7' )
#     print ( 'foo8' )
#     print ( 'foo9' )
#     print ( 'foo10' )
#     print ( 'foo11' )
#
# def bar():
#     print('bar1')
#     print ( 'bar2' )
#     print ( 'bar3' )
#     print ( 'bar4' )
#     print ( 'bar5' )
#     #time.sleep ( 1 )
#     print ( 'bar6' )
#     print ( 'bar7' )
#
# threading.Thread(target=foo,args=()).start()
# threading.Thread(target=bar,args=()).start()
#
# print('main')

def music(name):
    for i in range(2):
        print('i am bein to listen music:%s-->%s' % (name,datetime.datetime.now()))
        time.sleep(4)
        print('end to listen-->%s' % datetime.datetime.now())

def move(name):
    for i in range(2):
        print('i am bein to watch move:%s-->%s' % (name,datetime.datetime.now()))
        time.sleep(5)
        print('end to watch-->%s' % datetime.datetime.now())

print('start:%s' % time.time())
t1=threading.Thread(target=music,args=('许巍的故乡',))
t2=threading.Thread(target=move,args=('战狼2',))
threads=[t1,t2]
for i in threads:
    i.setDaemon(True) # 守护线程，如果设置了守护线程，当主线程执行完执行，这个线程就会结束掉，没有设置守护线程的那个线程不受影响
    i.start()
print('i:',i.getName())
#i.join()# 阻塞的作用，目的是为了让线程执行完之后再执行后面的主线程的代码
print('end:%s' % time.time())




