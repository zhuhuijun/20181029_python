# coding=utf-8
'''
1. only self or 1 /
2.1不是素数
'''
def is_p(t_int):
    if t_int == 1:
        return False
    elif t_int ==2 :
        return True
    else:
        for x in xrange(2,t_int):
            if t_int%2==0:
                return False
        return True


print(is_p(3))


