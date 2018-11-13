# author:gongnanxiong
# date:2018/11/12
import sys,time
# 进度条   file.flush()-->刷新当前缓冲区，把缓冲区的内容直接写到磁盘上去
# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(0.5)
#
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.5)

# r+ 读写模式  w+ 写读模式

f=open('file_ci','a+',encoding='utf-8')
f.seek(0)
print(f.readline())
print(f.tell())
#f.seek(f.tell())
# r+模式下，无论之前读的光标在哪个位置，下面写的时候也是默认写到文件的最后开始写
f.write('zhangfei')
f.close()
# w+模式下,生成file对象的时候直接先格式化整个内容,先写后读，读的内容默认从写的内容之后的光标开始，所以读到的数据为空，如果想读到写的内容，需要file.seek()
# a+模式下：直接读的话默认从内容最后开始，所以无法读出内容
# write  不管在什么模式下都是从文件最后开始写
