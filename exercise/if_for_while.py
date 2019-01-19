#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#int()  可以把str转换成相应的整数，类似atoi
s = input('input your birth year \n')
year = int(s)
if 1990 < year < 2000:
    print('90后')
elif year >= 2000:
    print('00后')
else:
    print('other')    
    
    

#range(5)   生成的序列是从0开始小于5的整数 区间[0, 5)
#再通过list()函数可以转换为list

#计算0+1+2+3+4
L = list(range(5))
sum = 0
for x in L:
    sum = sum + x
print('sum=',sum) #print把，替换成空格显示

sum = 0
i = 0
while i < 5:
    sum = sum + i
    i = i + 1
print('sum=%u' % sum)
