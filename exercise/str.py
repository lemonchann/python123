#!/usr/bin/env python3
#-*- coding: utf-8 -*-

x = 'ABC'
y = b'ABC'
print(x.encode('ascii'))
print(x.encode('ascii').decode('ascii'))
print(y.decode('ascii'))
print(y.decode('utf-8'))


print('中文字符'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#下面这种会报错
#print(b'中文字符'.decode('utf-8'))

#格式化输出，
print('i and %s have %u apple' % ('jim', 200))

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print( 'growth rate: %d%%' % 7)

#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print( 'Age: %s. Gender: %s' % (25, True))
