import random
print(random.random()) #f返回0-1之间的小数
print(random.randint(1,8)) #返回1-8之间的整数，包括8
print(random.randrange(0,10,2)) #范湖0-10之间，步长为2的整数，不包含10
print(random.sample([1,2,3,4],2)) #给定一个列表，返回列表中的几个
print(random.choice([1,2,3,4])) #返回列表中的任意一个元素

# shuffle 打乱列表的顺序
li=[1,2,3,4,5]
random.shuffle(li)
print(li)

#生成6位随机数,包含大小写，数字
def random_code():
    code=''
    for i in range(6):
        code+=str(random.choice([random.randrange(0,10),chr(random.randint(65,90)),chr(random.randint(97,122))]))
    return code

print(random_code())