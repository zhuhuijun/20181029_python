# coding=utf-8
import time
import threading
def a():
    print('a beign')
    time.sleep(2)
    print('a end')

def b():
    print('b beign')
    time.sleep(2)
    print('b end')

b_time = time.time()
a()
b()
print(time.time() - b_time)


b_time = time.time()
_a = threading.Thread(target = a)
_b = threading.Thread(target = b)
_a.start()
_b.start()
_a.join()
_b.join()
print(time.time() - b_time)
