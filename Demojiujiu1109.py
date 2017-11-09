
#coding=utf-8
#九九乘法表
m =1
while m<10:
    n=1
    while n<m:
        print n,'*',m,'=',m*n,"\t",
        n+=1
    if n==m or n>m:
        print n, '*', m, '=', m * n, "\n",
        m+=1