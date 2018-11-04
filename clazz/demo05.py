# coding=utf-8
class test():
    def d(self):
        print('this is d')
    @property
    def dd(self):
        return 'dd'
    @staticmethod
    def statcm():
        print('this is static method')

t = test()
t.d()
test.statcm()
print(t.dd)