#coding=utf-8
from  demo03 import MyLog
m = MyLog()
m.logDebug('fssssssssssssss')
class sth(object):
    def __init__(self,xixi):
        self.name = xixi
    def __enter__(self):
        print(u'hello,enter')
        return self.name
    def __exit__(self,type,value,trackbacke):
        print(u'hello,exit...')


with sth('fsfsfs') as s:
    print(s)