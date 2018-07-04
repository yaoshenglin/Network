#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

import socket
import threading
import time

encoding = "utf-8"

def socket_server():
    n = 0
    # 创建socket对象 (协议IP4，TCP)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # s.settimeout(3.0) #设置超时时间

    # 主机地址(0.0.0.0：绑定所有地址，127.0.0.1：绑定本机地址，外部计算机无法连接进来)
    host = '0.0.0.0'
    # host = socket.gethostname() # 获取本地主机名
    port = 9999

    # 监听端口(绑定到网卡)
    s.bind((host,port))
    # 设置最大连接数，超过后排队
    s.listen(5)

    while True:
        n = n + 1
        # 接收一个新连接
        sock,addr = s.accept()
        # 创建新线程处理TCP连接
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()
        if n == 2:
            t = threading.Thread(target=EndDes, args=("End",))
            t.start()
            break

def tcplink(sock,addr):
    print("Accept new conntection from %s:%s……"%addr)
    # 发送数据
    sock.send("欢迎学习Python网络编程!".encode(encoding))
    while True:
        # 接收消息
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode(encoding) == "exit":
            break
        sock.send(("Hello,%s!"%data.decode(encoding)).encode(encoding))
    # 关闭连接
    sock.close()
    print("Connection from %s:%s closed." % addr)

def EndDes(content):
    time.sleep(5)
    print(content)

socket_server()

