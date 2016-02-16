

# coding=utf-8
"""
测试scipy中的最小二乘法参数估计
"""

import numpy as np
from scipy.optimize import leastsq

#待拟合的函数，x是变量，p是参数
def fun(x, p):
    a, b = p
    return a*x + b

#计算真实数据和拟合数据之间的误差，p是待拟合的参数，x和y分别是对应的真实数据
def residuals(p, x, y):
    return fun(x, p) - y

#一组真实数据，在a=2, b=1的情况下得出
x1 = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y1 = np.array([3, 5, 7, 9, 11, 13], dtype=float)

#调用拟合函数，第一个参数是需要拟合的差值函数，第二个是拟合初始值，第三个是传入函数的其他参数
r = leastsq(residuals, [1, 1], args=(x1, y1))

#打印结果，r[0]存储的是拟合的结果，r[1]、r[2]代表其他信息
print r[0]