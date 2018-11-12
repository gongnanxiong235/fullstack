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
current_layer=location
previos_layers=[current_layer]
while True:
    for i in current_layer:
        print(i)
    choose=input("--->:").strip()
    if len(choose)==0:
        print("输入错误，请重新输入")
    elif choose=='fanhui':
        if len(previos_layers)==1:
            print("已经是最顶层，无法返回")
            break
        else:
            current_layer=previos_layers[-1]
            previos_layers.pop()

    elif choose=='quit':
        break
    elif not choose in current_layer:
        print("输入错误，请重新输入")
    else:
        if  isinstance(current_layer[choose],(dict,list)):
            previos_layers.append(current_layer)
            current_layer=current_layer[choose]
        else:
            print("已经是最后一层了")
            break
