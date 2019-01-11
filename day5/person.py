class person():
    def __init__(self,username,password):
        self.username=username
        self.password=password

    @property
    def name(self):
        return self.username

    @name.setter
    def name(self,value):
        self.username=value


class PageTation():
    def __init__(self,page):
        try:
            self.page=int(page)
        except:
            self.page=1
    @property
    def start(self):
        return (self.page-1)*10
    @property
    def end(self):
        return self.page*10

    def show(self):
        print("helloworld")
# hello=list(range(1000))
#
# while 3:
#     pagenumber=input("please enter the page")
#     page=PageTation(pagenumber)
#     print(hello[page.start:page.end])

page=PageTation(3)
helo=getattr(page,"end")
print(helo)