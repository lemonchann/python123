#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#example for List,一种有序列表
#定义一个空的list, len=0
L = []
print('empty L len=',len(L)) #输出空格代替，
print('empty L len=%u' % len(L))

L = ['first', 'second', 'third']
#用len()函数可以获得list元素的个数：
print('len(L)=', len(L))

#用索引来访问list中每一个位置的元素，记得索引是从0开始的
print('L[0]', L[0])
print('L[1]', L[1])
print('L[2]', L[2])

#还可以用-1做索引，直接获取最后一个元素
print('last elem in L:', L[-1])
#以此类推，可以获取倒数第2个、倒数第3个,倒数第四就越界了
print('last two elem in L:', L[-2])


#append 往list中追加元素到末尾
L.append('fourth')
print('after append:', L)

#pop删除末尾元素,要删除指定位置的元素，用pop(i)方法，其中i是索引位置
L.pop()
print('after pop:', L)

#list内的对象可以是不同类型
L_1 = ['first', 10, True]
print('L_1', L_1)

#list的元素可以是list
L.append(L_1)
print('new L:', L)

print('L_1[0]', L[-1][0])
print('L_1[1]', L[-1][1])
print('L_1[2]', L[-1][2])


#example for tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

#要定义一个只有1个元素的tuple, 不能用t = (1)
t = (1,)
print("t=", t)
