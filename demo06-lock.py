# coding=utf-8
import threading
mlock = threading.Lock()

num = 0
def a():
    global num
    mlock.acquire()
    num+=1
    mlock.release()
    print(str(num))

for i in range(0,10):
    d = threading.Thread(target=a)
    d.start()
    