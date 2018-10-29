# _*_coding=utf-8 _*_
def AAA():
    r = 0
    print('++++++START+++++++++')
    while r<5:
        yield 9
        print("[AAA] AAA r=%s" % r)
        r = r + 1
    print('+++++++END++++++++++')

for i in AAA():
    print(i)
    
"""
第二种情况：' x = yield 9 '

理解：和 print(1)的输出一样，但会在内存保存值；x 的值为 yield 保存值的 传递次数。

"""
def AAA1():
    r = 0
    print('++++++START+++++++++')
    while r < 3:
        x=yield 9
        print('[AAA] AAA r= %s' % r)
        print('[AAA] AAA x= %s' % x)
        r +=1 
        print('--第%s次循环结束--' %r)
    print('+++++++END++++++++++')
        
for i in AAA1():
    print (i)
"""
https://blog.csdn.net/weixin_32346335/article/details/64126794
"""


def AAA2():
    while True:
        print('[AAA2]-START')
        x=yield 9
        print('[AAA2]-x=%s' %x)
        print('[AAA2]-END')
def BBB2(a):
    print('[BBB2]-START')
    r = a.send(None)
    n=0
    while n < 3:
        n+=1
        r = a.send(n)
        print('[BBB2]-r=%s' %r)
        print('[BBB2]-第%s次循环END\n' %n)
    a.close()
BBB2(AAA2())
