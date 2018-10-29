# _*_ coding:utf-8 _*_
def func1(*nums):
    mymax = None
    mymin = None
    for x in nums:
        if isinstance(x,int):
            if mymax == None:
                mymax = x
                mymin = x
            else:
                mymax = max(mymax,x)
                mymin = min(mymin,x)
    return [mymax,mymin]
assert func1(1) == [1,1]