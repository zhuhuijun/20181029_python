# coding=utf-8
import threading
import time

mlock = threading.Lock()
num = 500


def a():
    global num
    for i in range(0, 100):
        mlock.acquire()
        num += 1
        mlock.release()

t = time.time()

lArr = []
for i in range(0, 10):
    d = threading.Thread(target=a)
    d.start()
    lArr.append(d)
for i in lArr:
    i.join()
print(u"total acount:%s\n" % str(num))
print("time cost:%s\n"%(time.time()-t))