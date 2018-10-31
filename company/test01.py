# _*_ coding=utf-8 _*_
from urllib import request


targeturl='http://tieba.baidu.com/p/1753935195'
def     get_html(targeturl):
    html = request.urlopen(targeturl)
    htmlcontent = html.read().decode('utf-8')
    return htmlcontent

if __name__ =="__main__":
    cont = get_html(targeturl)
    print(cont)
