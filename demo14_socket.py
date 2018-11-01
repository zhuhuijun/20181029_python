# _*_ coding=utf-8 _*_
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',8125))
server.listen(8)
# 代表最多请求8个
while 1:
    connection,address = server.accept()
    buf = connection.recv(1024)
    connection.send(buf)
server.close()


