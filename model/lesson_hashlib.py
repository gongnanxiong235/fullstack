# author:gongnanxiong
# date:2018/11/30

import hashlib

hello=hashlib.md5()
hello.update('helloworld'.encode("utf-8"))
print(hello.hexdigest())
hello.update('gongnanxiong'.encode('utf-8'))
print(hello.hexdigest())

hello2=hashlib.md5()
hello2.update('helloworldgongnanxiong'.encode('utf-8'))
print(hello2.hexdigest())
