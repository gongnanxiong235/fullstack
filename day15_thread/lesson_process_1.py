import multiprocessing,random,time,os,threading
def test(name):

    time.sleep(3)
    print('hello:%s' % name)

# if __name__ == '__main__':
#
#     processList=[]
#     for i in range(3):
#         process=multiprocessing.Process(target=test,args=('gong'+str(random.randint(0,100)),))
#         processList.append(process)
#     for j in processList:
#         j.start()
#     for k in processList:
#         j.join()


'''
自定义类的方式创建多进程
1.创建的所有进程都是主进程的子进程
2.在windows下，进程的代码必须写在if __name__ == '__main__': 下，不然会报错，liunx不会这样
3.多进程下的每个子进程是无法共享数据的，为了达到共享数据的目的，可以使用把要共享的数据(multiprocessing.quere)作为参数传递给另外一个队列的方式
'''
class MyProcess(multiprocessing.Process):
    #此构造方法中传递需要共享的数据queue，这样所有子线程只要以这种方式创建都可以共享这个数据
    def __init__(self,pname,queue):
        super(MyProcess,self).__init__()
        self.pname=pname
        self.queue=queue
    def run(self):
        # print(__name__)
        # print('parent:',os.getppid())#获取父进程
        # print('sin:',os.getpid())#获取当前进程
        test('gong'+str(random.randint(0,100)))
        self.queue.put(1)
        print(self.queue.qsize())#1 2 3 4 递增，说明了几个进程共享了一个队列（共享一个数据）


if __name__ == '__main__':

    processList=[]
    queue=multiprocessing.Queue()

    for i in range(6):
        processList.append(MyProcess('zhangsan',queue))# 传递的queue是为了共享这个数据，注意，直接传递只针对队列的数据类型
        processList[i].start()
    for j in processList:
        j.join()

    for i in range(queue.qsize()):
        print(queue.get())


'''
进程间的数共享方式(list.dict 等) 2 Manager
'''

class MyProcess(multiprocessing.Process):
    def __init__(self,ll):
        super(MyProcess,self).__init__()
        self.ll=ll
    def run(self):
        print('hello')
        self.ll.append(self.name)


if __name__ == '__main__':
    threads=[]
    with multiprocessing.Manager() as manager:
        ll= manager.list()

        for i in range(4):
            threads.append(MyProcess(ll))
            threads[i].start()
        for j in threads:
            j.join()
        for k in ll:
            print(k)










