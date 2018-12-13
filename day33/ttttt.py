# author:gongnanxiong
# date:2018/12/13


for i in range(10):
    if i==3 or i==5:
        continue
    for j in range(10):
        if j>=i:break
        else:
            if i+j>5:break
        print(i+j)
    if i==6:break


