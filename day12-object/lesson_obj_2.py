class Foo:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        pass

    '''
    print(Foo.__dict__)  #以字典的方式打印出类的所有成员
    '''
    #  print(int(foo))  相当于重写了int() 方法
    def __int__(self):
        return 3

    # print ( str ( foo ) ) 相当于重写了str（）方法
    def __str__(self):
        return '%s:%s岁 性别:%s' % (self.name,self.age,self.gender)

    # print(foo('callsss'))  对象加小括号的方式 自动调用
    def __call__(self, *args, **kwargs):
        return [x for x in args]

    # print(foo+Foo('lisi',20,'nan'))  可以用+
    def __add__(self, other):
        return str(self)+str(other)

    #析构方法，在对象销毁的时候调用
    def __del__(self):
        print('deling')

    # print(foo[10]) 类似列表的取值方法，重写的此方法，可以用obj[nunber]的方式返回数据
    # print(foo[10:20:2])  类似列表的分片的方法 其实这时候item其实是一乐slice类型，里面封装的三个值 start end step
    def __getitem__(self, item):
        if type(item) is int:
            print ( "按照索引的方式处理" )
        if type(item) is slice:
            print("按照分片的方式处理")

    # foo[10]=100  key可以对应的10  value对应的100
    def __setitem__(self, key, value):
        print(value+10)

    #  del foo[10] 重写此方法，
    def __delitem__(self, key):
        print(key)
    # 重写这个方法 表示对象是一个可迭代对象 所以可以用for循环 但是for循环是通过next方法是一个个的取值,所以用iter()
    def __iter__(self):
        return iter([1,2,3,4,5,6,7,8,9])

foo=Foo('zhangsan',30,'nan')
print(int(foo))
print(str(foo))
print(foo('callsss'))
print(foo+Foo('lisi',20,'nan'))

print(Foo.__dict__)  #以字典的方式打印出类的所有成员

print(foo[10])
print(foo[10:20:2])
foo[10]=100

del foo[10]

for i in foo:
    print(i)
