# author:gongnanxiong
# date:2018/11/22

with open('hello.txt','w',encoding='utf-8') as file_write:
    lines=['hello','world','gong','nan','xiong']
    lines=[x+'\n' for x in lines]
    file_write.writelines(lines)