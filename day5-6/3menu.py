
f=open('location','r+',encoding='utf-8')
str_loction=f.read()
f.close()
location=eval(str_loction)
print(location)
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
        print('currentlays:', type(current_layer))
        if isinstance(current_layer,dict):
            previos_layers.append(current_layer)
            current_layer=current_layer[choose]
            print('currentlays:',type(current_layer))
        else:
            print("已经是最后一层")
            break
