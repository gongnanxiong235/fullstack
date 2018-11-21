# author:gongnanxiong
# date:2018/11/13
print("我们都是中国人")
str="hello"
print('j' in str)

dict_hello={'hello':'world','abc':'def'}
print('hello' in dict_hello)
for i,v in dict_hello.items():
    print(i,v)

a=list(dict_hello)
print(a)
b=list(dict_hello.items())

c=range(5)
for i in c:
    print(i)