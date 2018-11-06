# author:gongnanxiong
# date:2018/11/6

count=0
while True:
    username=input("UserName:")
    password=input("Passworld:")
    if username=='gongnanxiong' and password=='123456':
        print("welcome %s" % username)
        break
    else:
        count+=1
        if count>3:
            break
        print("erro")