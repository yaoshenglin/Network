#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

import socket
import threading
import time

encoding = "utf-8"

def socket_udp_server():
    n = 0
    # 创建socket对象 (协议IP4，UDP)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 设定绑定地址
    host = '0.0.0.0'
    port = 80

    s.bind((host,port))

    while True:
        n = n + 1
        # 接收数据
        data,addr = s.recvfrom(1024)
        print("Received from %s:%s."%addr)
        # 发送数据
        s.sendto(b"hello,%s,welcome!"%data,addr)
        if n == 3:
            t = threading.Thread(target=EndDes, args=("End",))
            t.start()
            break

def EndDes(content):
    time.sleep(3)
    print(content)

socket_udp_server()

