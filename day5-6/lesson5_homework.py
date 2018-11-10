location={
    '江苏':{'苏州':['昆山','太仓','常熟','工业园区','吴中区'],
            '无锡':['宜兴','太湖区','江阴'],
            '南京':['鼓楼区','溧水区','江宁区','玄武区']},
    '广东':{'广州':['海珠区','番禺区','天河区','南沙区','增城区'],
            '深圳':['福田区','龙华区','南山区'],
            '汕头':['金平区','龙湖区','澄海区','朝阳区']},

    '浙江':{'杭州':['西湖区','下沙区','临平市','临安市','淳安县'],
            '湖州':['德清县','南浔区','高新区'],
            '嘉兴':['嘉善县','海盐县','南湖区','海宁市']},
    '山东':{'济南':['历下区','市中区','天桥区','平阴县','商河县'],
            '青岛':['市南区','市北区','黄岛区'],
            '济宁':['任城区','微山县','泗水县','梁山县']}
}

sheng=location.keys()
sheng_flag=True
shi_flag=True
xian_flag=True
while True:
    if sheng_flag==False or shi_flag==False or xian_flag==False:
        print("欢迎下次再来")
        break
    print("以下是可选省份")
    for i,v in enumerate(sheng,1):
        print(i,v)
    input_1=input("请输入省编号")
    if input_1=='quit':
        sheng_flag = False
        continue
    elif not input_1.isdigit():
        print("输入有误，请重新输入")
        continue
    elif int(input_1)<=0 or int(input_1)>len(sheng):
        print("输入有误，请重新输入")
        continue
    else:
        sheng_name=list(sheng)[int(input_1)-1]
        print(sheng_name)
        print('{name}省有以下管辖市'.format(name=sheng_name))
        shi_list=location[sheng_name]
        shi_name_list=[]
        for k in shi_list.keys():
            shi_name_list.append(k)
        for k ,j in enumerate(shi_name_list,1):
            print(k,j)
        while True:
            if xian_flag==False:
                break
            input_2=input("请输入市编号：")
            if input_2 == 'quit':
                shi_flag=False
                break
            elif input_2 == 'fanhui':
                break
            elif not input_2.isdigit():
                print("输入有误，请重新输入")
                continue
            elif int(input_2) <= 0 or int(input_2) > len(sheng):
                print("输入有误，请重新输入")
                continue
            else:
                choose_shi_name=shi_name_list[int(input_2)-1]
                xian_list=shi_list[choose_shi_name]
                print("%s市下面共有%s个县，分别是："%(choose_shi_name,len(xian_list)))
                for f,x in enumerate(xian_list,1):
                    print(f,x)
                xian_input=input('是否继续?输入任意键返回到上一级,输入quit退出程序:')
                if xian_input=='quit':
                    xian_flag = False
                    break
                else:
                    continue




