# -*- coding: utf-8 -*-

#Python 有方法将任何值转换为字符串：将它传递给repr()或str()函数

s = 'Hello, world.'
print 1,str(s)
print 2,repr(s)
print 3,str(1.0/7.0)
print 4,repr(1.0/7.0)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print 5,s
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print 6,hellos
# The argument to repr() may be any Python object:
print 7,repr((x, y, ('spam', 'eggs')))

#这里用两种方法输出平方和立方表：
for x in range(1, 11):  #rjust: 通过在左侧填充空格使字符串在给定宽度的列右对齐 类似的方法还有str.ljust()和str.center()
    print repr(x).rjust(2), repr(x*x).rjust(3),repr(x*x*x).rjust(4)

for x in range(1,11):   #0，1，2 占位符  2d，3d，4d 字符宽度
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

#另外一种方法 str.zfill()，它向数值字符串左侧填充零
print 8,'12'.zfill(5)
print 9,'-3.14'.zfill(7)  #包含浮点
print 10,'3.14159265359'.zfill(5)  #如果超过填充长度不需要填充

#str.format()方法的基本用法
print 11, 'We are the {} who say "{}!"'.format('knights', 'Ni')
# 0,1 位置参数  决定了输出顺序
print 12,'{0} and {1}'.format('spam', 'eggs')  #spam and eggs
print 12,'{1} and {0}'.format('spam', 'eggs')  #eggs and spam
#food，adjective 关键字参数
print 13,'This {food} is {adjective}.'.format(
     food='spam', adjective='absolutely horrible')  #This spam is absolutely horrible.

import math
print 14, 'The value of PI is approximately {0:.3f}.'.format(math.pi)   #3.142  0:.3f控制浮点数长度

#open()返回一个文件对象，最常见的用法带有两个参数：open(filename, mode)。
#f = open('workfile', 'w')
#print f
#要读取文件内容，可以调用f.read(size) ，该方法读取若干数量的数据并以字符串形式返回其内容
#f.readline()从文件读取一行数据
#f.write(string)将 string 的内容写入文件中并返回None。

