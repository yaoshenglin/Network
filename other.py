#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'YSL-PC'

with open('weibo.txt','r',encoding='utf-8') as f:
    content = f.read()
    dicInfo = eval(content)
    print(dicInfo)