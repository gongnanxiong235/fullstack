# author:gongnanxiong
# date:2018/11/9


a=list(('zhangsan','lisi','wangwu'))
print(a)
b=dict([['age','49'],('name','zhangsan')])
print(b)
#setdefault:如果key存在，不做任何改变，如果key不存在，增加键值对；此方法返回值=value
print(b.setdefault('job','it'))
b.setdefault('age','30')
print(b)
# print(b['hello'])-->如果key不存在，会报错
# print(b.get('hello'))-->如果key不存在，返回None
# print(b.get('hello','zhangsan'))-->如果key不存在，返回默认值
# print(b.keys())--返回所有key的集合，非序列(dict_keys类型)，需要转换
# print(list(b.values()))--需转换成列表才能用

d={'hello':'world'}
b.update(d)#类似于列表的extend方法，把两个组合成一个
print(b)
# a.pop(2)
# print(a)

# b.pop('hello')
# b.popitem()--->随机删除一个键值对，并以元祖方式返回删除的键值对
# # print(b)

# dict1=dict.fromkeys(['h1','h2','h3'],'hello')--->默认值是none，可以指定默认值（是一个浅拷贝，改变一个key的值，其他key的value也会跟着一起改变）
print(dict1)