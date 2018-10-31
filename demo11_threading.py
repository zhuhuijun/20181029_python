# _*_ coding=utf-8 _*_
import threading
import time
"""
习题:
已知列表 info=[1,2,3,4,55,3444]
生成6个线程每次输出一个值，最后输出the end
"""

def test(args):
    time.sleep(0.01)
    print(args)

info=[1,2,3,4,55,344]
thres=[]
for i in range(0,len(info)):
    thi = threading.Thread(target=test,args=[info[i]])
    thi.start()
    thres.append(thi)
for i in thres:
    i.join()
print('the end')

