

'''
metaclass：所有类的祖宗，也就是所有类创建的时候 metaclass=type
万物皆对象，所以，一个类也是一个对象
1.class Foo(metaclass=MyType):  表示创建Foo类的时候metaclass 由type 类变为MyType类去处理
2.程序执行到MyType类的时候，先执行MyType类的的init方法
3.Foo()的时候执行 MyType类中的call方法 obj=self.__new__(self, *args, **kwargs)，其中这里的self是Foo类--》return object.__new__(cls, *args, **kwargs)
  执行完后obj=object.__new__(cls, *args, **kwargs)  创建了一个对象
4.self.__init__(obj)  再调用Foo类的构造方法

总结  一个对象创建的时候的顺序为 call--new--init

'''

class MyType(type):
    def __init__(self,*args,**kwargs):
        print('MyType:init')
        pass
    def __call__(self, *args, **kwargs):
        print('MyType:call')
        obj=self.__new__(self, *args, **kwargs)
        self.__init__(obj)
        pass

class Foo(metaclass=MyType):
    def __init__(self):
        print ( 'FOO: init' )
        pass

    def __new__(cls, *args, **kwargs):
        print('FOO: new')
        return object.__new__(cls, *args, **kwargs)

obj=Foo()
