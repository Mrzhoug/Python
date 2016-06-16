# -*- coding: utf-8 -*-
def fib(n):
    a,b=0,1
    while a<n:
        print a,
        a=b
        b=a+b
#fib(2000)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

#ask_ok (' Do you really want to quit? ')  #不完全参数输出
#ask_ok('OK to overwrite the file?', 2)   #不完全参数输出
#ask_ok ('OK to overwrite the file?', 2, 'Come on, only yes or no!')  #完全参数输出

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put" , voltage , "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
#parrot(1000)                                          # 接收一个必要参数
#parrot(voltage=1000)                                  # 接收一个必要参数
#parrot(voltage=1000000, action='VOOOOOM')             # 接收一个必选参数和一个可选参数
#parrot(action='VOOOOOM', voltage=1000000)             # 接收一个必选参数和一个可选参数 顺序不一致
#parrot('a million', 'bereft of life', 'jump')         # 一个必选参数和两个可选参数
#parrot('a thousand', state='pushing up the daisies')  # 一个必选参数和一个可选参数

#以下会报错
#parrot()                     # 参数缺失
#parrot(voltage=5.0, 'dead')  # 没有填入必选参数
#parrot(110, voltage=220)     # 多次填入必选参数
#parrot(actor='John Cleese')  # 未知的可选参数

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:             # *接收一个包含所有没有出现在形式参数列表中的位置参数元组
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())     #先进行关键字排序  **传入字典的形式的参数列表接收一个字典，该字典包含了所有未出现在形式参数列表中的关键字参数
    for kw in keys:
        print kw, ":", keywords[kw]

#调用
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#编码风格
#
#
#使用 4 个空格的缩进，不要使用制表符。
#4 个空格是小缩进（允许更深的嵌套）和大缩进（易于阅读）之间很好的折衷。制表符会引起混乱，最好弃用。
#折行以确保其不会超过 79 个字符。
#这有助于小显示器用户阅读，也可以让大显示器能并排显示几个代码文件。
#使用空行分隔函数和类，以及函数内的大块代码。
#如果可能，注释独占一行。
#使用 docstrings。
#运算符周围和逗号后面使用空格，但是括号里侧不加空格： a = f(1, 2) + g(3, 4)。
#命名您的类和函数一致 ；惯例是使用驼峰命名法的类和使用lower_case_with_underscores 的函数和方法 。始终使用self作为方法的第一个参数的名称（关于类和方法的更多信息请参见初识类）。
#如果希望你的代码在国际化环境中使用，不要使用奇特的编码。简单的 ASCII 在任何情况下永远工作得最好。

