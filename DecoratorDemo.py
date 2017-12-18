#!/usr/bin/python
# -*- coding: UTF-8 -*-
#copy from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000#0

import time, functools
def log(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrappers(*args, **kw):
            if arg != func:
                print('%s call %s' % (arg, func.__name__))
            else:
                print('call %s' % func.__name__)
            return func(*args, **kw)
        return wrappers
    if isinstance(arg, str):
        return decorator
    else:
        return decorator(arg)


@log("aaa")
def fast1(x, y):
    time.sleep(0.0012)
    return x + y
@log
def fast2(x, y):
    time.sleep(0.0012)
    return x * y

print fast1(1,2)
print fast2(2,3)
