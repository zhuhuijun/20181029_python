# coding=utf-8
import threading

mlock = threading.Lock()
num = 500


def a():
    global num
    for i in range(0, 100):
        mlock.acquire()
        num += 1
        mlock.release()


for i in range(0, 10):
    d = threading.Thread(target=a)
    d.start()
    d.join()
print(u"总长为:%s" % str(num))
