# -*- coding: utf-8 -*-
#学习String
print 1,r'C:\Python\name'   #\n会被认定为转义字符  加上r会按照原始字符串输出
print 2,'''\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
'''     #加上\号将不会输出第一行 (示例中第一个会输出换行)
print 3,3 * 'un' + 'ium'   #输出3次‘un’然后和‘ium’连接
print 4,'Py''thon'  #不用+号，会自动连接
text = ('Put several strings within parentheses '
            'to have them joined together.')
print 5,text  #加上（）会自动连接成一句话
word="Python"
print 6,word[0]  #  'P'  可以根据索引值来获取字符
print 7,word[-1] #  'n'  也可以根据负值来获取字符，但是从后面开始获取 负值索引从-1开始
print 8,word[:3] #  'Pyt' 索引从0-2的字符
print 9,word[3:] #  'hon' 索引从3-最后的字符
print 10,word[-2:] # 'on' 索引从倒数第二个开始直到末尾的字符
print 11,word[4:45] # 'on' 如果单取字符word[45]会报错：下标越界  但遇到切片，会自动处理
#字符串不能根据下标赋值，
str='s'+word[1:]
print 12,str
print 13,len(str)  #内置函数len
#学习Unicode
strs= u'Hello\u0020World !Hello World !' #用Unicode的格式输出
print 1,strs
strs=ur'Hello\\u0020World !'#只有在小写的'u'前面有奇数个反斜杠，才会用上面的uXXXX 转换
print 2,strs
