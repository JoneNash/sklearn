#!/usr/bin/env python
# -*- coding:utf-8 -*-

'this is a module test'

__author__='JoneNash'



#and:如果布尔上下文中的所有值都为真，那么 and 返回最后一个值;布尔上下文中的某个值为假，则 and 返回第一个假值。
#or:如果有一个值为真，or 立刻返回该值。如果所有的值都为假，or 返回最后一个假值。
#and or 都是自左向右运算.
#类似于java中的 return (x > 1) ? x * fact(x - 1) : 1 ;  用法
def fact(x):
    return x > 1 and x * fact(x - 1) or 1
print fact(6)

print fact(3)

print 6>7 and 6*5 or 1



#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性

class Student():
    pass

def setAge(self,age):
    self.age=age

s=Student();
s.name='Tom'
print s.name

from types import MethodType

s.setAge=MethodType(setAge,s,Student);

s.setAge(18)

print s.age

def setHome(self,home):
    self.home=home

Student.setHome=MethodType(setHome,None,Student)

s2=Student()
s2.setHome('beijing')

print s2.home

#s2未赋予动态方法
# s2.setAge(18)
# print(s2.age)

#__slots__ 限定class的属性

class GraduateStudent(object):
    __slots__=("name","age")

    test = 'hello'

    def __init__(self, test):
        self.__test=test

    _home = None

    def get_home(self):
        return self._home
    def set_home(self, home):
        self.test=home




gs=GraduateStudent('hi')
#以下为错误示范
# gs.oldhome="beijing"
# print gs.oldhome
#oldhome

#错误示范
# gs._home="beijing"


# gs.set_home("in beijing")
print "home"
print gs._home
# print gs._home
gs.set_home("test")

print gs.get_home()

