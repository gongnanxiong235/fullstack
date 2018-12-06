# author:gongnanxiong
# date:2018/12/6


'''
python的多继承:
1.左侧优先，就是根据继承父类的顺序去找对用的方法
2.一条道走到底，就是左侧父类找不到的时候再去左侧父类的父类中去找，找不到再去右侧的父类中找，再走到右侧父类的父类，以此类推
3.如果左右侧有一个共同的根时（顶层有一个公共的父类）,根最后执行
'''

class GradeFather(object):
    def g1(self):
        print('g1')
    def g2(self):
        print('g2')

class Father(GradeFather):
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
    def f3(self):
        print('f3')
    def f4(self):
        print('f4')
    def g2(self):
        print('father g2')

class Son(Father):
    def s1(self):
        print('s1')
    def s2(self):
        print('s2')
    def s3(self):
        print('s3')
    def s4(self):
        print('s4')
    def f1(self):
        super(Son,self).f1() # 调用父类的方法
        Father.f2(self) #调用父类的方法
        print('self')
        print('------')
        super(Father,self).g1()
        super(Son, self).g1()
        print('--------')

son=Son()
son.f1()
son.f2() # 继承后可以用父类的方法
son.g1() # 父类找不到可以到父类的父类中寻找
son.g2() # 自身类没有方法，先去父类中找，如果父类中找到了 就不去父类的父类找了


class Foo:

    def __init__(self):
        self.name='zhangsan'

    def aaa(self):
        print('hello111111')

    county='china' #  在类中定义的字段，可以用类名直接调用，也可以用对象调用，因为是公共的 所以当一个对象改变值后其他对象调用结果是改变后的值
    @staticmethod  #  静态方法 参数不需要self 类名直接调用
    def sta():
        print('static method')
    @classmethod   #  类方法，其实就是静态方法的变种，用类名直接调用，调用的时候内部自动把当前类传入
    def clsm(cls):
        print(cls.county)

    @property     #  属性，相当于JAVA中的get方法 调用的时候不用加括号 例如 foo.name  只读
    def name(self):
        return self._name  # _name在这里==name 这是一种内部使用的固定方法，在赋值的时候如果不用_name 会报错，造成死循环

    @name.setter   #  属性，相当于JAVA中的set方法，调用的时候不用加括号 如果没有此方法，通过foo.name=value 会直接报错(属性名.setter) 可写
    def name(self,value):
        self._name=value

    @name.deleter  # 属性名.deleter -->表示可删除
    def name(self):
        print('hello')

    age=property(fget=aaa)#  属性的另一种表达方式 == @property 装饰


foo=Foo()
print(foo.name)
foo.name='lisi'
print(foo.name)

foo.age


'''
面向对象实现分页
'''
class PageTation:
    def __init__(self,page):
        try:
            self.page=int(page)
        except Exception :
            self.page=1
    @property
    def start(self):
        return (self.page-1)*10

    @property
    def end(self):
        return self.page * 10

li=[x for x in range(1000)]
while True:
    page=input('请输入页码:')
    if page=='quit':
        break
    tation=PageTation(page)
    print(li[tation.start:tation.end])

