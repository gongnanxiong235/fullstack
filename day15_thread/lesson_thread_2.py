import threading,time

'''
自定义线程类
'''
class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__(self)
        self.num=num

    #重写父类的run方法，当执行start方法的时候自动调用run方法
    def run(self):
        print('hello',self.name)

MyThread(1).start()
MyThread(2).start()

'''
线程安全，同步锁
1.加锁可以防止线程的不安全，加锁加在线程不安全的一段代码之间，如果在等个方法的代码加锁，等于串行
2.例如银行取钱一样。一个账户有多张卡，防止同一时刻有几个人一起取钱，这样账户就会错   只有一个人在取钱（结算的瞬间）锁住，等结算完之后再解锁，这样账户才安全
'''
num=100
lock=threading.Lock()# 获得锁的对象
def hello():
    global num
    print('ooo')
    lock.acquire()# 加锁
    temp=num
    time.sleep(0.001)
    #print('ok')
    num=temp-1
    lock.release()# 解锁
    print('''eee''')

threadList=[]
for i in range(100):
    t=threading.Thread(target=hello)
    t.start()
    threadList.append(t)

# 让所有线程都执行完才执行后面主线程的代码
for x in threadList:
    x.join()

print(num)

'''
生产者和消费者threading.Condition()
Condition:线程间的交互,niotify  wait

event=threading.Event:功能和Condition相似,都可以进行线程间的交互
event.set()==event.isSet():True
event.clean():Flase

'''

import random
baoziList=[]
lock_cond=threading.Condition()# 获得一把锁，默认是Rlock（递归锁）
class Producter(threading.Thread):
    def run(self):
        # global  baoziList   #  全局变量如果是个列表。则无需声明global
        while True:
            baoziNumber=random.randint(0,1005555)
            print('%s 生产出了一个包子，包子代号为%s' %(self.name,baoziNumber))
            lock_cond.acquire()
            baoziList.append(baoziNumber)
            print('包子个数为：%s' % len(baoziList))
            lock_cond.notify()
            lock_cond.release()
            time.sleep(2)


class cunstomer(threading.Thread):
    def run(self):
        while True:
            lock_cond.acquire()
            if baoziList.__len__()==0:
                lock_cond.wait() # 释放线程。等着，一直到有线程通知
            print('%s 吃掉了一个包子，这个包子是%s' %(self.name,baoziList[-1]))
            baoziList.pop()
            lock_cond.release()
            time.sleep(0.25)


threads=[]
for i in range(5):
    threads.append(Producter())
threads.append(cunstomer())

for j in threads:
    j.start()

















