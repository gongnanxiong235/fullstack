from urllib.request import urlopen
import gevent,time
from gevent import monkey
import ssl
#python 3.6 在使用urllib连接https的时候回报错：urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)>
ssl._create_default_https_context = ssl._create_unverified_context
monkey.patch_all() # 最大程度的去监听IO阻塞，这样协程会切换的更快，从而达到提高速度的目的


# 最基础的爬虫代码
def func(url):
    print('GET %s' % url)
    openp=urlopen(url)
    data=openp.read()
    print('%s is end' % url)
    # with open ( 'xiaohua.html', 'wb' ) as f:
    #     f.write ( data )

#data=func('http://www.xiaohuar.com')
# urllist=['http://www.xiaohuar.com','https://www.sina.com.cn','http://www.sohu.com']
start=time.time()
# for i in urllist:
#     func(i)


# 爬虫因为是IO 阻塞型程序，所以用协程的方式会更快
gevent.joinall([gevent.spawn(func,'http://www.xiaohuar.com'),
                gevent.spawn(func,'https://www.sina.com.cn'),
                gevent.spawn(func,'http://www.sohu.com')])

print('耗时：%s' % (time.time()-start))
