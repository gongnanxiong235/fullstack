dict1=dict((('name','zhangsan'),('age',30),('job','it')))
print(dict1)
# print(tuple(dict1.items()))-->字典转换成元组（列表）
print('hello'.count('l'))

# print('hello'.index('u'))--如果找不到会报错
# print('hello'.find('u'))--如果找不到返回-1

# a=[1,2,3,4]
# print(a.index(5))

# 格式化字符串的另一种方法
b='my name is {names},and Iam {age} years old,and you?'
print(b.format(names='gongnanxiong',age=32))
print(b.format_map({'names':'gongnanxiong','age':32}))
print(b.format_map(dict([('names','gongnanxiong'),('age',32)])))


# print(b.format_map(dict([('name','gongnanxiong'),('age',32)])).capitalize())--把首字母转换成大写
print(b.endswith('?'))
print(b.startswith('my'))


def fibs(number):
    result =[0,1]
    for i in range(number-2):
        result.append(result[-1]+result[-2])
    return result
for i in fibs(10):
    print(i)

x='hello,world,gongnanxiong,nihao'
print(x.split(','))
print(x.rsplit(','))

