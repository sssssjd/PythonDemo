#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 使用map，reduce将str转化为float

from functools import reduce


def mm(m):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[m]


def nn(i, j):
    return i*10+j


def str2float(s):
    n1 = s[::-1].find('.')
    n2 = s[::].find('.')
    s = s[:n2]+s[n2+1:]
    f = reduce(nn, map(mm, s))
    for e in range(n1):
        f = f/10
    return f


print(str2float("0.005"))
