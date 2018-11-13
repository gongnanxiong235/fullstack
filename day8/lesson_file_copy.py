# author:gongnanxiong
# date:2018/11/13
import os
copy_path='file_ci_copy'
if not os.path.exists(copy_path):
    print("file is not exit")
else:
    open(copy_path,'a+',encoding='utf-8')

# a+模式下，如果打开的文件不存在，则自动创建一个(但是又不想执行一次机就追加一次)
with open('file_ci','r',encoding='utf-8') as file_read,open(copy_path,'w+',encoding='utf-8') as file_write:
    for line in file_read:
        file_write.write(line)