#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#dic就是c++的map类型

#初始化
dic = {'first':1, 'second':2, 'third':3}
print(dic)
print('dic[first]=', dic['first'])

#add
dic['fourth'] = 4
print(dic)

#modify
dic['fourth'] = 5
print(dic)

#delete
dic.pop('fourth')
print(dic)

#find
#一是通过in判断key是否存在
if 'first' in dic:
    print(True)
else:
    print(False)

#二十通过dict提供的get方法，如果存在返回对应的value
#如果key不存在，可以返回None，或者自己指定的value
print(dic.get('second'))
print(dic.get('test', 'not exist'))


#set就是c++的set set可以看成数学意义上的无序和无重复元素的集合

#dic和set的key type都要求是const的
#在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
#而list是可变的，就不能作为key


