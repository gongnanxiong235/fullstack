# author:gongnanxiong
# date:2018/11/26

'''
参数作为对象进行传递
'''

def func_hello(number):
    if number%2==0:return number*number
    else:return number+2

def func_hello_2(a,b,fun):
    return fun(a)+fun(b)


result=func_hello_2(2,3,func_hello)
print(result)


'''
推导式列表
'''

list_a=[x for x in range(5)]
print(list_a)

list_b=[x for x in list_a if x%2==0]
print(list_b)

list_c=[[1,2,3,4],[5,6,7,8]]
list_d=[j*j for x in list_c for j in x  if j>=5]
print(list_d)


'''
推导式字典
'''

list_dict_a=[1,3,5,7,9]
dict_b={key:value for key,value in enumerate(list_dict_a)}
print(dict_b)
dict_c={key:value for key,value in enumerate(reversed(list_dict_a))}
print(dict_c)

'''
推导式集合
'''
set_a={x*x+2 for x in range(10) if x&2==0}
print(set_a)

'''
map函数
返回一个map类型的需要用list转换一下
'''
def func_map(string):
    return str(string).upper()

map_a=map(func_map,['hello','world'])
print(list(map_a))

'''
filter
'''

def func_filter(content):
    return str(content).isdigit()

def func_filter_2(n):
    if n=='a':return False
    else:return True

filter_a=filter(func_filter,['hello',123,'234','world'])
print(list(filter_a))
print(list(filter(func_filter_2,['a','b','c','d'])))



'''
reduce(fun,lst)函数：必须是两个参数
把fun执行的结果交给lst中的下一个参数继续执行
'''
from functools import reduce
def func_reduce(a,b):
    return a+b

reduce_a=reduce(func_reduce,range(1,101))
print(reduce_a)

#sum()
print(sum([1,2,3,4,5,6]))

# 元素只要包含None 0 ‘’ 都返回false 其余都返回True
print(all([1,None]))

'''
函数式编程
'''

#用reduce实现阶乘
print(reduce(lambda x,y:x*y,range(1,4)))

#用lamda表达式实现map强大的功能
print(list(map(lambda a:str(a).upper(),['a','b','c','d'])))