#!/usr/bin/python
# -*- coding: UTF-8 -*-

width = int(raw_input('输入对角线长度：'))
for row in range(width + 1):
    for col in range(width + 1):
        if ((abs(row - width/2) + abs(col - width/2)) == width/2):
            print "*",
        else:
            print " ",
    print " "