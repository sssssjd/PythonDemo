#!/usr/bin/python
# -*- coding: UTF-8 -*-

#  请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#  ax2 + bx + c = 0(a!=0)的两个解。

import cmath


def quadratic(a, b, c):
    for i in a, b, c:
        if not isinstance(i, (int, float)):
            raise TypeError('int or float')

    if a == 0:
        raise SyntaxError("error! a != 0")

    d = b ** 2 - 4 * a * c  # b**2 为b的平方
    if d < 0:
        return "error无解"
    elif d >= 0:
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        return x1, x2


print(quadratic(2, 3, 1))  # =>  (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)