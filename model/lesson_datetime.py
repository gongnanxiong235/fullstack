import datetime
import time

'''

datetime.datetime

'''
# 当前的时间
now=datetime.datetime.now()
print(now)
print(type(now))

# 转换成datetime.datetime类型
now_now=datetime.datetime(2018,11,24,11,55,57)
print(now_now)
print(type(now_now))

# 当前的时间
date_today=datetime.datetime.today()
print(date_today)
print(type(date_today))

# 时间戳转换为datetime
str_date=datetime.datetime.fromtimestamp(time.time())
print(str_date)
print(type(str_date))

# 把datetime.datetime转化为指定格式的字符串时间
hello=datetime.datetime.strftime(now_now,'%Y/%m/%d %X')
print(hello)
print(type(hello))

# 把字符串转换为datetime.datetime 对象
hello_date=datetime.datetime.strptime(hello,'%Y/%m/%d %X')
print(hello_date)
print(type(hello_date))

# 星期几
print(hello_date.isoweekday())

# datetime.datetime转换为元组时间 从而可以转换为时间戳
tup_hello_date=datetime.datetime.timetuple(hello_date)
print(tup_hello_date)
hello_timestamp=time.mktime(tup_hello_date)
print(hello_timestamp)


'''
datetime.date
'''
# 当前日期
date_today=datetime.date.today()
print(date_today)

# 把日期转换成date.date对象
date_hello=datetime.date(2019,11,24)
print(date_hello)

# date转换为字符串格式化时间
date_str=datetime.date.strftime(date_today,'%Y-----%m-----%d')
print(date_str)

# date转换成元组时间
date_timestamp=datetime.date.timetuple(datetime.date.today())
print(date_timestamp)

# a=datetime.timedelta(days=-1)
# b=datetime.datetime.now()
# print(b.day)
# c=a+b
# print(c)
# print(type(c))
# d=datetime.datetime.strftime(c,'%Y-----%m-----%d')
# print(d)

'''
timedelta：只支持增加减少按日和周，不支持年和月
两个datetime.datetime相加或者减的结果是一个timedelta对象
timedelta对象可以调用属性或者相差多少天，多少秒 多少毫秒

'''
# 增加5周
datetime.timedelta(weeks=5)
d1 = datetime.datetime.strptime('2017-10-16 19:21:22', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
# 两个日期相差多少天
print((d2-d1).days)


'''
pip install boto3
relativedelta：支持相差年 月  天  周  等
'''
from dateutil.relativedelta import relativedelta
# from django.utils import timezone
t1 = datetime.datetime.now()
neww_year = t1 + relativedelta(years=5,days=3,months=6)
print(neww_year)


def get_weekly(*args):
    return datetime.datetime(*args).isoweekday()


print(get_weekly(2018,11,25,12))