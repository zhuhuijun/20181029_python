# _*_ coding=utf-8 _*_
'''
mushup
scrapy

'''
from wsgiref.simple_server import make_server
def demo_app(environ,start_response):
    from StringIO import StringIO
    stdout = StringIO()
    print >>stdout ,"Hello World"
    print >>stdout
    '''
    h = environ.itmes();h.sort()
    
    for k,v in h:
        print >>stdout,k,'=',repr(v)
    '''
    for i in environ:
        print >>stdout,i,'=',environ[i]
    start_response('200 OK',[('Content-Type','text/plain')])
    return [stdout.getvalue()]
if __name__=='__main__':

    httpd = make_server('',8997,demo_app)
    sa = httpd.socket.getsockname()
    print ('Serving HTTP ON %s,Port:%d'%(sa[0],sa[1]))

    import webbrowser
    webbrowser.open('http://localhost:8997/xyz?abc')
    #httpd.handle_request()
    httpd.serve_forever()