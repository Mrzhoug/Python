# -*- coding: utf-8 -*-
squares = [1, 4, 9, 16, 25]
print 1,squares
print 2,squares[1] ,squares[-2] ,squares[3:] #同样支持正索引和负索引切片
squares=squares+[2,3,5,6,7,8]   #在后面追加列表
print 3,squares
squares.append(216)
print 4,squares   #也可以使用append()
squares[2:5]=[]  #删除2-4
print 5,squares
print 6,range(5, 10,2)  #5 起始值，10 终止值 2 步长

a = [66.25, 333, 333, 1, 1234.5]
print 7,a.count(333), a.count(66.25), a.count('x')
a.insert(2, -1)
a.append(333)
print 8,a
print 9,a.index(333)
a.remove(333)
print 10,a
a.reverse()
print 11,a
a.sort()
print 12,a
print 13,a.pop()
print 14,a

#filter(function, sequence)返回的序列由function(item)结果为真的元素组成。如果sequence是一个字符串或元组，结果将是相同的类型；否则，结果将始终是一个列表
def f(x): return x % 2 != 0 and x % 3 != 0   #定义函数返回不能被2和3整除的数
print 15, filter(f, range(2, 25))

#map(function, sequence) 为序列中的每一个元素调用 function(item) 函数并返回结果的列表。

def cube(x): return x*x*x   #计算列表中所有元素的立方值：
print 16,map(cube, range(1, 11))

#可以传入多个序列；此时，传入的函数也必须要有和序列数目相同的参数，执行时会依次用各序列上对应的元素来调用函数（如果某个序列比另外一个短，就用 None 代替）
seq = range(8)
def add(x, y): return x+y
print 17,map(add, seq, seq)

#reduce(function, sequence) 只返回一个值，它首先以序列的前两个元素调用函数 function，然后再以返回的结果和下一个元素继续调用，依此执行下去。
# 例如，若要计算数字 1 到 10 的总和：
def add(x,y): return x+y
print 18,reduce(add, range(1, 11))

#字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print 19,tel
print 20,tel.keys()

#遍历技巧
#遍历一个序列时，使用enumerate()函数可以同时得到索引和对应的值。

for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v,

#同时遍历两个或更多的序列，使用zip()函数可以成对读取元素。

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

#要反向遍历一个序列，首先正向生成这个序列，然后调用 reversed() 函数。
for i in reversed(xrange(1,10,2)):
    print i,

#要按排序顺序循环一个序列，请使用sorted()函数，返回一个新的排序的列表，同时保留源不变。

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f

#遍历字典时，使用iteritems()方法可以同时得到键和对应的值。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

#若要在循环内部修改正在遍历的序列（例如复制某些元素），建议您首先制作副本。在序列上循环不会隐式地创建副本。切片表示法使这尤其方便：
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
       words.insert(0, w)




