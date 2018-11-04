# coding=utf-8
class boy(object):
    gender = 1
    """docstring for boy"""
    def __init__(self, name):
        self.name = name
class girl(object):
    gender = 0
    def __init__(self, name):
        self.name = name    

class love(object):
    def __init__(self, fir, sen):
            self.fir= fir
            self.sec = sec
    def meet(self):
        print('this is meet %s and %s meet'%(self.fir.name,self.sec.name))
    def marry(self):
        print('this is marry %s and %s meet'%(self.fir.name,self.sec.name))
        pass
    def children(self):
        print('this is children %s and %s meet'%(self.fir.name,self.sec.name))
        pass

class normallove(love):
    """docstring for normal"""
    def __init__(self, first,second):
        pass