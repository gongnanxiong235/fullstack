# author:gongnanxiong
# date:2018/11/21

class MyIter:
    def iter(self,seq):
        self.seq=seq
        self.flag=0
        return self
    def next(self):
        seq_leth=len(self.seq)
        if not self.flag>seq_leth-1:
            next_number = self.seq[self.flag]
            self.flag+=1
        else:
            return
        return next_number


# my_iter=MyIter()
# my_iter.iter([1,3,5,7,9])
# print(my_iter.next())
# print(my_iter.next())
# print(my_iter.next())
# print(my_iter.next())
# print(my_iter.next())
# print(my_iter.next())


a=iter([1,3,5,7,9])
for i in range(5) :
    print(next(a))
