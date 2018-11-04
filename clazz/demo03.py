# coding=utf-8
class Base(object):
    """docstring for Base"""
    def __init__(self, name):
        self.name = name

class B(Base):
    """docstring for B"""
    def get_name(self):
        print(self.name)
        return self.name
b = B('aa')
b.get_name()