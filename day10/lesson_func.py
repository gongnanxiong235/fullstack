'''
1.参数位置优先级.必须参数>默认参数>可变参数（*>**）
2.调用参数的时候必须遵循形参的顺序，但是如果用key=value的方式则不需要顺序
3.可变参数方法反转：元组：*（）或者*[]  字典：**{key:value}
'''

def func_1(name='zhangsan',age=18):
    print('%s:%s' % (name,age))

func_1(age=32,name='gongnanxiong')


def func_2(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

func_2(1,2,3,4,5)
func_2(*[1,2,3,4,5])#反转


def func_3(**kwargs):
    for i,v in kwargs.items():
        print('%s:%s' %(i,v))

func_3(name='zhangsan',age=18,job='it')
keys=['name','age','job']
values=['zhangsan',18,'it']
# 反转   zip：把两个列表对应组成一个item的列表
func_3(**dict(zip(keys,values)))


def out(A):
    def inner(B):
        return A+B
    return inner


a=out(5)(2)
print(a)

