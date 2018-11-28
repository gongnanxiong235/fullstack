# author:gongnanxiong
# date:2018/11/6

# count=0
# while True:
#     username=input("UserName:")
#     password=input("Passworld:")
#     if username=='gongnanxiong' and password=='123456':
#         print("welcome %s" % username)
#         break
#     else:
#         count+=1
#         if count>3:
#             break
#         print("erro")


# for i in range(3):
#     username=input ( "UserName:" )
#     password=input("Passworld:")
#     if username == 'gongnanxiong' and password == '123456':
#        print("welcome %s" % username)
#        break
#     else:
#         print("账户名或密码错误")
#
# #for else-----for循环中没有打断的时候回执行else
# else:
#     print("输入次数太多了")

a=dict([["iphone",5800],["mac",9000],["coffic",32],["python book",30],["bike",1500]])
print(a)

#同时给对个变量赋值
c,d=[1,2]
print(c)
print(d)

#把列表转换成带索引的元组(带参数代表从多少开始)
f=enumerate([["iphone",5800],["mac",9000],["coffic",32],["python book",30],["bike",1500]],1)
for i,v in f:
    print(i,v)

def hello():
    print('hello')
