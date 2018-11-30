# author:gongnanxiong
# date:2018/11/12

# f=open('file_ci','r',encoding='utf-8')
# content=f.read()
# print(content)
# f.close()
#
# f2=open('file_ci','a',encoding='utf-8')
# f2.write('\nhello world')
# f2.writelines(['\ndiyuhang','\ndierhang'])
# f2.close()
#
#
# f3=open('file_ci','r+',encoding='utf-8')
# print(f3.read())
# f3.write('\n ++++++++++++++++')
#



# f3.close()
# f=open('file_ci','r+',encoding='utf-8')
# comtents=f.readlines()
# print(comtents)
# for i in comtents:
#     if i=='\n':continue
#     print(i.rstrip())
# f.close()

f=open('file_ci','r+',encoding='utf-8')
# comtents=f.readlines()
# for i,v in enumerate(comtents,1):
# #     if i==3:v="".join((v.rstrip(),'++++++'))
# #     print(v.rstrip())
# # f.close()

for i in f:
    if i.startswith('hello'):
        i="---".join((i.rstrip(),'hello'))
    print(i.rstrip())
f.close()
