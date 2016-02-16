# coding=utf-8

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# 可以通过传递一个list对象来创建一个Series，pandas会默认创建整型索引

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 1)通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame
dates = pd.date_range('20160101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 2)通过传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)

print('----head----')
print(df.head())
print('----tail----')
print(df.tail(3))
print('-----index----')
print(df.index)
print('-----columns----')
print(df.columns)
print('-----describe 未绑定------')
print(df.describe)
print('-----describe()-----')
print(df.describe())
print('-----Translation-----')
print(df.transpose())
#获取
print('------col-----')
print(df['A'])
print('-----row-----')
print(df[0:3])
print('-----row-----')
print(df['20160101':'20160103'])

# 通过标签选择

print('---选择多个col---')
print(df.loc[:,['A','B']])
print('---交叉区域---')
print(df.loc['20160101':'20160103',['A','B']])
print('-----通过标签选择----')
print(df.loc[dates[1]])
print('---维多缩减--')
print(df.loc['20160101',['A','B']])
print(' ----获取一个标量-----')
print(df.loc['20160101','A'])
print(' ----获取一个标量-----')
print(df.at[dates[0],'A'])

print(' ----mean-----')
print(df.mean())
print(' ----mean-----')
print(df.mean(1))

#categorical

df3=pd.DataFrame({"id":[1,2,3,4,5,6],"raw_grade":['a','b','b','a','a','e']})
print('-------grade bef-------')
df3["grade"] = df3["raw_grade"].astype("category")
print(df3["raw_grade"])
print(df3["grade"])
print('-------grade after-------')
# df3["grade"].cat.categories = ["very good", "good", "very bad"]
# print(df3["grade"])
print('--------------')
df3["grade"] = df3["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df3["grade"] )
df3.sort_values(by="grade")
print(df3)


#---------------

#list 可变链表
classmates_list = ['Michael', 'Bob', 'Tracy']
#tuple 不可变数组
classmates_tuple = ('Michael', 'Bob', 'Tracy')
#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Adam'] = 67
print d

if('Thomas' in d):
    print d['Thomas']
else:
    print('d do not have Thomas')


d.get('Thomas')
d.get('Thomas', -1)


#空函数
def nop():
    pass


#参数检查
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print my_abs(-199)

#返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x,y

#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)

#多参数
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('tom','male',9,city='tianjin')

#可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4))

tup=[1,2,3,4]
print(calc(*tup))


#关键字参数,关键字参数有什么用？它可以扩展函数的功能
def person(name,age,**kw):
    print 'name:',name,' age:' ,age,'other:',kw
person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

#参数组合,参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(10)