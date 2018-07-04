#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

import socket

encoding = "utf-8"

def socket_client():
    # 创建socket对象 (协议IP4，TCP)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    port = 9999

    # 连接服务器，指定主机和端口(必须是双元素组)
    s.connect((host, port))
    # 接收消息
    data = s.recv(1024)
    print(data.decode(encoding))

    for dataStr in ['小萌','小智','小强']:
        # 发送数据
        s.send(dataStr.encode(encoding))
        data = s.recv(1024)
        print(data.decode(encoding))
    s.send(b'exit')
    s.close()

socket_client()