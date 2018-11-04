# coding=utf-8
class Student(object):
    def __init__(self,val):
        self.val = val

    def get(self):
        print(self.val)
        return self.val
d = Student('fsfsf')
d.get()
print('122')
