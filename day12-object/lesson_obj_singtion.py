class SingTion:
    instan=None

    def __init__(self,name):
        self.name=name
    def __new__(cls, *args, **kwargs):
        if cls.instan is None:
            cls.instan=cls.__init__(name)
        return cls.instan


a=SingTion('zhangsan')
b=SingTion('lisi')
print(a==b)

