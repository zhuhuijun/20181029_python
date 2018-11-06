#coding=utf-8
from  demo03 import MyLog
m = MyLog()
class MyException(Exception):
    def __init__(self,error,msg):
        self.args=(error,msg)
        self.error = error
        self.msg = msg
try:
    raise MyException(1,"fsfsfsf")
except Exception as e:
    print(str(e))
    m.logDebug(str(e))