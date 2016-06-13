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





