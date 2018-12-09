
'''
反射
1.getattr setattr delattr  这三个方法构成了反射
2.反射方法中的obj 可以是一个对象，一个类，一个模块等

'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__hello=3

    def show(self):
        print('%s-%s--%s' %(self.name,self.age,self.__hello))

peson=Person('zhangsan',30)
#获取属性的三种方式
print(peson.name) # 通过对象获取

print(peson.__dict__['name']) # 先得到对象的字典，再从字典中通过字符串取值

print(getattr(peson,'name'))  # 反射的方式getattr（obj，key）

getattr(peson,'show')()  # 反射的方式也可以获取到方法

setattr(peson,'gender',getattr(peson,'show'))  # 反射的方式赋值
peson.gender()

delattr(peson,'gender')  # 删除成员
#peson.gender()  # AttributeError: 'Person' object has no attribute 'gender'
#getattr(peson,'__hello')

