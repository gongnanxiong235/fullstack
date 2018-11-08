# author:gongnanxiong
# date:2018/11/7

# a=['zhangsan','lisi','wangwu','zhaoliu']
# a.sort(key=len,reverse=False)
# print(a)
# print('zhangsan' in a)

products_list=[["iphone",5800],["mac",9000],["coffic",32],["python book",30],["bike",1500]]
money=int(input("你现在有多少钱"))
shop_list=[]
product_index = ''
while True:
    if product_index=='quit':
        break
    print("以下是产品列表，请选择你要买的商品：")
    for i in range(len(products_list)):
        print("%s: %s-->%s元"  % (i+1,products_list[i][0],products_list[i][1]))

    while True:
        product_index = input("请输入商品编号")
        if product_index=="quit":
            print(shop_list)
            break
        elif not product_index.isdigit() or int(product_index)==0 or int(product_index)>len(products_list):
            print("输入有误，请重新输入")
        else:
            if money < products_list[int(product_index) - 1][1]:
                    print("钱不够，请重新选择")
            else:
                    shop_list.append(products_list[int(product_index)-1])
                    money-=products_list[int(product_index)-1][1]
                    print("还剩下%s块钱" % money)







