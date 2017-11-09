#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 迭代 10 到 20 之间的数字类型
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'


# 输出 2 到 100 简的质数
prime = []
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
print prime


# 打印空心等边三角形
rows = int(raw_input('输入行数：'))
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print " * ",
        elif i == rows - 1:
            if k % 2 == 0:
                print " * ",
            else:
                print "   ",
        else:
            print "   ",
    print "\n"

# 打印菱形
width = int(raw_input('输入对角线长度：'))
for row in range(width + 1):
    for col in range(width + 1):
        if ((abs(row - width/2) + abs(col - width/2)) == width/2):
            print "*",
        else:
            print " ",
    print " "