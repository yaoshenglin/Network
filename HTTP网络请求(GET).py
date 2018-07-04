#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

from urllib import request

def get_request():
    r = request.urlopen("http://www.baidu.com")
    print('Status:', r.status, r.reason)
    for k,v in r.getheaders():
        print("%s:%s" % (k, v))
    data = r.read()
    r.close()
    print("Data:", data.decode('utf-8'))

get_request()