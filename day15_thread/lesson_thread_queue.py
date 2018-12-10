

'''
队列：quewue：默认数据结构中加了锁，所以线程是安全的
1.默认是先进先出
2.默认可以放无限数据,queue.Queue(10)加上参数代表限定了容量
3.当限定了容量，容量满后再去put就会造成线程阻塞put(1) 可以使阻塞变成抛出异常
4.队列因为是线程安全的，所以多用在多线程中，单线程中建议使用列表，元组等

'''
import threading,queue,random,time
baizilist=queue.Queue(10)# 不带参数表示这个队列可以放无穷大的数据,加参数限定了容量
class Producter(threading.Thread):
    def run(self):
        while True:
            baozi=random.randint(1000000,100000045)
            print('生产出了%s号包子' % baozi)
            baizilist.put(baozi)
            time.sleep(2)


class Customer(threading.Thread):
    def run(self):
        while True:
            b=baizilist.get()
            print('吃掉了%s号包子'% b)
            time.sleep(0.2)


threads=[]
for i in range(5):
    threads.append(Producter())
threads.append(Customer())

for j in threads:
    j.start()

