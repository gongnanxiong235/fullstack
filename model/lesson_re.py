import re

'''
元字符
'''
ss='hello world'
rs=re.findall('w..sssl',ss) # .可以代表任何字符（除了换行符）,但是只能代表一个字符
print(rs)

rs=re.findall('^h...o','hfdsjijdsighdihellofsdfd')# ^ ：只从字符串的开始开始匹配，所以这个表达式的结果是空
print(rs)

rs=re.findall('h...o$','hfdsjijdsighdihellofsdfd')# ^ ：只从字符串的最后匹配，所以这个表达式的结果是空
print(rs)

rs=re.findall('b.*b','jfidsjfibfidjfidjfijdifjdifbfjdijfidsjfibfjdfjsdifjdsb')  # .* 代表中间是任意个数的任意字符
print(rs)

rs=re.findall('bf*i','jfidsjfibfffffidjfidjfijdifjdifbfjdijfidsjfibfjdfjsdifjdsb') # bf*i 代表b开头，中间有0个以上的任意个数的f，最后是i（*：匹配0到多次）
print(rs)

rs=re.findall('bb+f','jfidsjfibbbbbbfffffidjfidjfijdifjdifbfjdijfidsjfibfjdfjsdifjdsb') # +:代表匹配一个以上的字符,'bb+f':代表b开始，中间有一个及以上的b，以f结尾的字符串
print(rs)


rs=re.findall('b?f','jfidsjfibbbbbbfffffidjfidjfijdifjdifbfjdijfidsjfibfjdfjsdifjdsb') #? :  只能匹配到0-1次
print(rs)

rs=re.findall('b{1,5}f','jfidsjfibbbbbbfffffidjfidjfijdifjdifbfjdijfidsjfibfjdfjsdifjdsb') #  :  {}代表匹配范围，两个数字代表范围，一个数字代表匹配多少次
print(rs)

rs=re.findall('a[b,c,e]x','acx') # [b,c,e] 代表范围，，相隔代表或的关系  匹配结果:['acx']
print(rs)

rs=re.findall('a[a-z]x','acx') # [a-z] 代表范围，a-z之间所有小写字母
print(rs)

rs=re.findall('a[a,*,^,{,}]x','a^x') # 元字符遇到中括号，元字符的功能取消，及就是个普通字符
print(rs)

rs=re.findall('[^45]','dfdsf4512dfdg') # ^ 在中括号中表示取反 [^45] 表示除了 4 和5  效果和[^4,5]是一样的
print(rs)


'''
\ 遇上元字符，去除元字符的功能
  遇上普通字符，有些普通字符有特殊含义
1.\d 代表【0-9】 \D 代表【^0-9】
2.\s 代表任何空白字符  \S 代表任何非空白字符
3.\w 代表任何数字字母==[0-9a-zA-Z] \W 代表非数字字母==[^0-9a-zA-Z]
4.\b 与特殊字符的边界
'''

print(re.findall('135\d{4}5555','fdfdfijnnvdif13599995555'))  # 135开头，5555 结尾，中间是0-9的数字 总共4位数
print(re.findall('\s\d','fdfdfijnnvdif13 59 999 55 55')) #匹配空白加数字
print(re.findall(r'I\b','Hello I am a LIST')) # 空格 & 等都是特殊字符
print(re.findall('a\.','a.dfdf')) #. 遇上\ 就是普通的一个点

print(re.findall('www.(\w+).com','www.baidu.com')) # 分组后的结果只是分组的内容 ：['baidu']
print(re.findall('www.\w+.com','www.baidu.com'))
print(re.findall('www\.\w+\.com','www.baidu.com'))
print(re.findall('www.(?:\w+).com','www.baidu.com'))  #在分组中加上?:的功能是取消分组的权限(分组的权限是匹配出的结果只是分组的内容)


'''
re的常用方法

match(规则,字符串) 只在开始匹配规则，满足返回对象，不满足返回None
split(规则,字符串) 通过规则分割字符串 注：先匹配第一个，并分割，再从第一个分割后的匹配第二个，并分割。。。
sub(规则,新内容,字符串) 通过规则匹配字符串内容，并把匹配结果替换成新内容
compile(规则) 将规则封装一个对象中，下次可以直接用对象查询，不需要输规则
finditer(规则,字符串)将查找的结果成一个迭代器,使用next方法取,每个内容用group再取数
'''

ret=re.search('a\w+','hfhdjahfdjhfa1212adjfiksjdfa ') # 返回的ret是个对象
print(ret.group())  # 取值，注意：sesch方法只匹配第一次  如果没有只 ret对象是个None


#re.match()  # 只在行首匹配，匹配不到返回None  与'^hello'的功能一样
#re.compile('\w+')返回一个规则对象 可以用这些规则对象再去调用其他re的方法 这些方法后面就只需要加一个待匹配的字符串，无需加规则了
print(re.sub('hel{2}]o','love','hhhellofdfdfhellofdsfdherhello'))

# ip = '192.168.266.1'
# # a = re.findall(r'^(?:\d\.|\d\d\.|1\d{2}\.|2[0-4]{1}\d\.|25[0-5]{1}\.){3}(?:\d|\d\d|1\d{2}|2[0-4]{1}\d|25[0-5]{1})',ip)
# # print(a)