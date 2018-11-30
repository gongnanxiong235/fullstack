# author:gongnanxiong
# date:2018/11/30

import os
'''
print(os.getcwd()) #获取当前工作目录str
os.chdir('/Users/gongnanxiong/gnx/fullstack/fullstack/model/test')   #切换到指定工作目录
print(os.getcwd())
os.chdir('../..')#切换到上一层目录（上上层目录）
print(os.getcwd())
print(os.listdir('/Users/gongnanxiong/gnx/fullstack/fullstack/model/')) #列出当前路径下的所有文件及文件夹
'''

# os.mkdir('./test/test1') #创建空文件夹 如果路径不存在则会抛出异常
# os.makedirs('./test/test1/test2/test3') #递归创建多层目录
# os.remove('./test/test.txt')  # 删除文件，如果路径下的文件不存在抛出异常，如果是个文件夹抛出异常
# os.removedirs('./test/test1/test2/test3') #从最后一层目录往上删除空文件夹 如果遇到不为空的文件夹则停止
# os.rmdir('./test') # 删除单个文件夹,如果文件夹下存在文件则抛出异常
# os.rename('./modify/hello.txt','./modify/hello1.txt') #修改文件和文件夹的名称
# os.system('cd') #执行shell命令
print(os.curdir) #当前目录
print(os.pardir) # 父目录
print(os.sep) #返回当前系统的路径分割符
# os.makedirs('%s%shell1%shello2' %(os.curdir,os.sep,os.sep)) #替代字符串的路径  因为各个操作系统的当前目录表示方法和路径分隔符不一样
print(os.linesep)  #返回当前系统的换行符
print(os.name) #返回操作系统的名称
print(os.path.abspath('./modify/hello1.txt')) #返回绝对路径

'''
os.path.
'''

print(os.path.basename('./modify/test1/test2/test3'))  #返回当前路径的最后一个文件/文件夹 名
print(os.path.dirname('./modify/test1/test2/test3'))  #去掉文件名，单独返回路径名

print(os.path.split('./modify/test1/test2/test3'))  # 分离路径与最后一个文件或者文件夹 组成一个元祖
print(os.path.splitext('./modify/test1/hello1.txt')) #分离路径名与最后一个文件的后缀组成一个元祖
print(os.path.getsize('./modify/hello1.txt'))  #以字节为单位返回当前文件的大小


'''
返回bool类型
'''
print(os.path.isdir('./modify/hello1.txt'))  #判断是否文件夹
print(os.path.isfile('./modify/hello1.txt')) #判断是否文件
print(os.path.exists('./modify/hello1.txt')) #判断路径是否存在
print(os.path.isabs('./modify/hello1.txt'))  #判断是否绝对路径
