import threading
import time

'''
多线程：
1.由于python的解释器Cpython 有一把大锁（GIL）导致，python使用多线程只能使用一个CPU，且同一时刻只能支持一个线程工作
2.python在处理IO密集型（阻塞,睡眠）的时候，用多线程可以提高效率，以为一个线程在阻塞的时候另一个线程可以抢占CPU资源处理另外的事情
3.python在处理计算密集型的时候，用多线程无法提高效率，因为几个线程用同一个CPU 且是轮换着工作，不但无法提高效率，且有可能比单线程慢，因为切换线程也需要时间
'''
def foo():
    print( 'foo1' )
    print ( 'foo2' )
    print ( 'foo3' )
    print ( 'foo4' )
    print ( 'foo5' )
    print ( 'foo6' )
    #time.sleep(1)
    print ( 'foo7' )
    print ( 'foo8' )
    print ( 'foo9' )
    print ( 'foo10' )
    print ( 'foo11' )

def bar():
    print('bar1')
    print ( 'bar2' )
    print ( 'bar3' )
    print ( 'bar4' )
    print ( 'bar5' )
    #time.sleep ( 1 )
    print ( 'bar6' )
    print ( 'bar7' )

threading.Thread(target=foo,args=()).start()
threading.Thread(target=bar,args=()).start()

print('main')




