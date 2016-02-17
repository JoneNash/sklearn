#!/usr/bin/env python
# -*- coding:utf-8 -*-

'this is a module test'

__author__='JoneNash'

#OOP三大法:封装、继承、多态


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


bart =Student('Bart Simpson',79)
lisa=Student('lisa Simpson',99)

bart.print_score()
lisa.print_score()

print bart.name


#继承与多态

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

dog1=Dog()

dog1.run()
print  isinstance(dog1, Animal)


#“开闭”原则——对扩展开放：允许新增Animal子类；对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

def run_twice(Animal):
    Animal.run()
    Animal.run()

run_twice(Dog())


#获取对象信息

import types

print type(dog1)

print type(int)==type(str)==types.TypeType

print 'dog1 is an animal :' ,isinstance(dog1,Animal)

#判断一个变量是否是某些类型中的一种
print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))

print dir(dog1)

class Cat(Animal):
    def __len__(self):
        return 100

print Cat().__len__()



