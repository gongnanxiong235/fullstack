# author:gongnanxiong
# date:2018/11/13
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("我们都是中国人")