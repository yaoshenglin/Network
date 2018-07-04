#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

import socket

# 创建socket对象 (协议IP4，TCP)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'www.baidu.com'
port = 80
# 连接服务器，指定主机和端口(必须是双元素组)
s.connect((host,port))
# 发送数据(一般服务器都有其标准格式)
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')

# 开始接收数据，指定每次最大接收数
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()
# 将接收的数据分离为HTTP头和网页内容
header,html = data.split(b'\r\n\r\n',1)
print(header.decode("utf-8"))
# 保存内容
with open('baidu.html','wb') as f:
    f.write(html)