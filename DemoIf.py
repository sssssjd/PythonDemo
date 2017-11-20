#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 根据BMI公式（体重除以身高的平方）计算BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖


while 1:
    s = raw_input ("身高(cm):")
    if s.isdigit():
        s = float(s)
        break
    else:
        print '输入错误，只接受整数，请重新输入！'
    continue

while 2:
    t = raw_input ("体重(kg):")
    if t.isdigit():
        t = float(t)
        break
    else:
        print '输入错误，只接受整数，请重新输入！'
    continue

BMI = t/s/s*10000

if BMI<18.5:
    print "BMI=%.2f, 低于18.5，属于：过轻。" % BMI
elif 18.5 <= BMI < 25:
    print "BMI=%.2f, 位于18.5-25，属于：正常。" % BMI
elif 25 <= BMI < 28:
    print "BMI=%.2f, 位于25-28，属于：过重。" % BMI
elif 28 <= BMI < 32:
    print "BMI=%.2f, 位于28-32，属于：肥胖。" % BMI
elif BMI >= 28:
    print "BMI=%.2f, 高于32，属于：严重肥胖。" % BMI