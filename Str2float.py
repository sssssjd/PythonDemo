#!/usr/bin/python
# -*- coding: UTF-8 -*-

#使用map，reduce将str转化为float


def m(m):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[m]
def n(i,j):
    return i*10+j
def str2float(s):
    n1 = s[::-1].find('.')
    n2 = s[::].find('.')
    s = s[:n2]+s[n2+1:]
    f = reduce(n,map(m,s))
    for e in range(n1):
        f = f*0.1
    return f

print(str2float('0.0005'))
