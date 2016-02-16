# coding=utf-8

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[1:3]
L2=range(100)
print(L2)
print L2[::5]
print (0, 1, 2, 3, 4, 5)[:3]
print 'ABCDEFG'[::2]

#迭代 只有迭代对象才可以使用迭代操作

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print d.get(key)
for value in d.values():
    print 'value:',value
for i, value in enumerate(['A', 'B', 'C']):
     print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)

from collections import Iterable
# str是否可迭代
print isinstance('abc', Iterable)


#列表生成器

L=[]
#循环式
for x  in range(1,11):
    L.append(x * x)
print(L)
#列表生成式
L=[x * x for x in range(1, 11)]
print(L)

#使用两层循环，可以生成全排列
L2=[m + n for m in 'ABC' for n in 'XYZ']
print L2

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s, str) else s for s in L]

#生成器  一边循环一边计算的机制，称为生成器（Generator）

g = (x * x for x in range(10))
for i in g:
    print i

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        if n>=5 :#设定结束项
            return ;

for i in fib(10):
    print i

