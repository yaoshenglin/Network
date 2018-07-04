#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

import socket
import time

encoding = "utf-8"

def socket_udp_client():
    # 创建socket对象 (协议IP4，UDP)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 获取本地主机名
    host = socket.gethostname()
    port = 80

    for dataStr in ['小萌','小智','小强']:
        # 发送数据
        s.sendto(dataStr.encode(encoding),(host,port))
        # 接收数据
        data = s.recv(1024)
        print(data.decode(encoding))
        time.sleep(0.5)
    s.close()

socket_udp_client()