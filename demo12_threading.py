# coding=utf-8
import urllib
import threading
import re

'''
已知列表info=['http://www.sina.com','http://www.sohu.com','http://www.163.com']
用多线程的方式打开列表的url,输出页面的状态码

'''
def get_code(url):
    html = urllib.urlopen(url).read()
    re_title='<title>(.*)</title>'
    title = re.findall(re_title,html)
    #print(html)
    print(title[0])

info=['http://www.sina.com','http://www.sohu.com','http://www.baidu.com']
thresds=[]
d = xrange(0,len(info))
for i in d:
    thr = threading.Thread(target=get_code,args=[info[i]])
    thr.start()
    thresds.append(thr)
for i in thresds:
    i.join()
print('ok')