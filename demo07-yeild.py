#coding=utf-8
'''
协程入门

'''
def test():
    i = 0
    a = 4
    while i<a:
        x = yield i
        i +=1
'''        
for i in test():
    print(str(i))
'''
t = test()
print(t.__next__())

