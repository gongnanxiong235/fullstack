import time


'''
总结：
1.字符串时间和时间戳之间都可以通过元组时间进行互转
2.时间戳转换为元组时间用localtime  和gmtime
3.元组时间转换为时间戳用mktime
4.元组时间转换为字符串时间用strftime
5.字符串时间转换为元组时间用strptime


'''
# 当前时间的时间戳
current_timestamp=time.time()
print(current_timestamp)

# 本地时间的元组时间time.struct_time，不带参数表示当前时间戳，也就是time.time
current_locatetime=time.localtime()
print(current_locatetime)

# 格林威治时间，与本地时间相差8小时
cureent_gztime=time.gmtime()
print(cureent_gztime)

# 传入一个时间戳，返回时间戳对应的元组时间
hello_localtime=time.localtime(1533023011.1203551)
print(hello_localtime)

# 返回字符串时间，不穿参数默认为time.localtime(time.time())
str_time=time.strftime('%Y-%m-%d %X')
print(str_time)

#strftime方法接收一个格式化样式和一个元组时间，把元组时间转化成一个对应格式的字符串时间
hello_str_time=time.strftime('%Y-%m-%d %X',hello_localtime)
print(hello_str_time)

# 把一个字符串时间转换成一个元组时间
strp_time=time.strptime(hello_str_time,'%Y-%m-%d %X')
print(strp_time)

# 把元组时间转换成时间错
print(time.mktime(strp_time))

# 把字符串时间转换成时间戳
print(time.mktime(time.strptime('2018-11-24 09:49:45','%Y-%m-%d %X')))

# 元组时间转化为结构化时间
asctime=time.asctime(time.localtime(time.time()))
print(asctime)

#时间戳转化为结构化时间
ctime=time.ctime(time.time())
print(ctime)

# 从元组中提取属性值
print(hello_localtime.tm_year)

# time.sleep(2)  睡眠