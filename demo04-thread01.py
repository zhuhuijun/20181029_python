# coding=utf-8
'''
1、全局锁是一个很重要的概念
在任意一个制定的时间有且只有一个线程在运行->python是线程安全的
线程安全歧义
2、多线程是复杂的不建议使用
3、io操作用到多线程
acquire
release
rlock()//重入锁
'''
import threading
num = 0
def t():
    global num
    num +=1
    print(str(num))
for i in range(0,10):
    d = threading.Thread(target = t)
    d.start()