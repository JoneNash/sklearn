#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy

#python实现
def pythonsum(n):
    a=range(n)
    b=range(n)
    c=[]

    for i in range(len(a)):
        a[i]=i**2
        b[i]=i**3
        c.append(a[i]+b[i])
    return c

print pythonsum(5)

#numpy实现

def numpysum(n):
    a=numpy.arange(n)**2
    b=numpy.arange(n)**3
    c=a+b
    return c

numpyresult=numpysum(5)
print numpyresult

#查看返回值类型
print type(pythonsum(5))
print type(numpysum(5))
print numpyresult.shape


###多维数组
mm=numpy.array([numpy.arange(2),numpy.arange(2)])

mm[0][0]=10
print mm
print "----------"
mmm=numpy.array([[numpy.arange(2),numpy.arange(2)],[numpy.arange(2),numpy.arange(2)]])

mmm[0][0][0]=12

print mmm

print type(mmm)

print( type(numpy.int8(8)))

#自定义数据类型

t=numpy.dtype([('name',numpy.string_,40),('numitems',numpy.int32),('price',numpy.float32)])
print t

# x=t("Tom",22,0.11)

# print x
#使用自定义流程
dt3=numpy.dtype([('f1', numpy.int32), ('f2', numpy.float)])
a=numpy.array([(1,2),(3,4)],dtype=dt3)
print a
print a.dtype

b=numpy.array([(1,2,3),(4,5,6)],dtype=t)
print b

#索引
a=numpy.arange(9)
print a[3:7]
#切片
print a[0:8:2]


#多维数组切片与索引

a=numpy.arange(24).reshape(2,3,4)
print a
print type(a)

print(a[:,1,1])
print a[0,:,:]
print a[0,1,::3]
print "-----"
b=numpy.arange(6)
print  a[::-1]
print  b[::-1]

a=numpy.arange(24).reshape(2,3,4)
print

c=numpy.array([numpy.arange(6),numpy.arange(6)])
print c.ravel()
print c.flatten()
print c.reshape(12)
a.shape=(24)
print a

#数组组合

a=numpy.arange(9).reshape(3,3)
b=2*a
print "-----a----"
print a
print "-----b----"
print b

#水平组合,最低维度(第一维)组合
print "------hstack-----"
print numpy.hstack((a,b))
#垂直组合,最高维度(第二维)组合
print "------vstack-----"
print numpy.vstack((a,b))
#深度组合,升维
print "------dstack-----"
print "深度组合:",numpy.dstack((a,b))

print "深度组合的单个元素:",numpy.dstack((a,b))[0][0][0]
#列组合
print  numpy.column_stack((a, b)) == numpy.hstack((a, b))

#行组合
print numpy.row_stack((a,b)) == numpy.vstack((a, b))


#数组分割
print "————————数组分割——————"
print a
#横向分割,在底维度分割
print "----横向分割-----"
print numpy.hsplit(a,3)
print numpy.split(a,3)[1]
#纵向分割,在高维度分割
print "----纵向分割-----"
print numpy.vsplit(a, 3)
#深度分割,相同位置元素组合
print "----深度分割-----"
c = numpy.arange(27).reshape(3, 3, 3)
print numpy.dsplit(c,3)
print "-----0------"
print numpy.dsplit(c,3)[0]
print c.ndim
print c.size
print c.itemsize
print c.size*c.itemsize
#三维转置,由1\2\3维的顺序改为了3\2\1维的顺序
print c.T

a=numpy.arange(9).reshape(3,3)
print a
print a.T

#数组转换,numpy的数组与python的list做相互转换
a=numpy.arange(9)
print a
print a.tolist()
b=numpy.array(a.tolist())
print b









