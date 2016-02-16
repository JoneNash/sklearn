# coding=utf-8
import math

#高阶函数:既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
f=abs
print f(-11)
def add(x, y, f):
    return f(x) + f(y)
print add(-11,12,f)

#map reduce
def fn(x,y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))

#过滤
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

#判断素数

def isPrime(n):
    if n==1 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
print 7,isPrime(7)

#排序
L=[36, 5, 12, 9, 21]
print sorted(L)

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted(L,reversed_cmp)

#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f()


#闭包.返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#错误示范
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

#正确示范
def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             return j*j
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

#正确示范——lambda函数版

f1,f2,f3=[(lambda x=i:x*x) for i in range(1,4)]
print f1(), f2(), f3()


#匿名函数-lambda函数  匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
def build(x, y):
    return lambda: x * x + y * y

print build(2,3)()

#装饰器
# #1.0
# def log1(func):
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper
#
# @log1
# def now():
#     print '2013-12-25'
#
# now()
#
# #2.0
# def log2(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log2('execute')
# def now():
#     print '2013-12-25'
#
# now()
#
# print now.__name__


#3.0 完整写法

import functools

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log3('execute')
def now():
    print '2013-12-25'

now()

#测验

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'begin call %s' % func.__name__
        returnValue = func(*args, **kw)
        print 'end call %s' % func.__name__
        return returnValue
    return wrapper

@log
def now():
    print '2015-9-26'
    return 'return value of func now'

#now = log(now)
print now()


#装饰器

from functools import wraps

GLOBAL_NAME = "Brian"

def print_name(para=None, name=GLOBAL_NAME):
    def actual_decorator(function):
        @wraps(function)
        def returned_func(*args, **kwargs):
            print "My name is " + name
            return function(*args, **kwargs)
        return returned_func

    if not para:    # User passed in a name argument
        def waiting_for_func(function):
            print('call function:waiting_for_func')
            return actual_decorator(function)
        return waiting_for_func

    else:
        return actual_decorator(para)

@print_name
def a_function():
    print "I like the name!"

@print_name(name='Matt')
def another_function():
    print "Hey, that's new!"

a_function()
print('*******')
another_function()


#####偏函数
import functools
int2 = functools.partial(int, base=2)
print int2('10010')
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数

max2=functools.partial(max,20)
print max2(5,7,19)


