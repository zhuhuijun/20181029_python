# coding=utf-8
import threading
def test():
    print(1)
ts=[]
for i in range(0,15):
    th = threading.Thread(target=test)
    ts.append(th)
for i in ts:
    i.start()
for i in ts:
    i.join()
    
a = threading.Thread(target=test)
b = threading.Thread(target=test)
a.start()
b.start()
a.join()
b.join()
