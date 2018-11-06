#coding=utf-8
from demo03 import MyLog
import os
m = MyLog()

def read_file(filepath):
    file = open(filepath,'r')
    try:
        all_text = file.read()
    except IOError as e:
        m.logDebug(str(e))
    else:
        return all_text
    finally:
        file.close()
text = read_file('test.log')
print(text)

def read_file2(filepath):
    with open(filepath) as file:
        all_text = file.read()
        return all_text
text = read_file2('test.log')
print(text)