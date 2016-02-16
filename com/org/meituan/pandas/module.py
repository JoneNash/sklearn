#!/usr/bin/env python
# -*- coding:utf-8 -*-

'this is a module test'

__author__='JoneNash'

import sys
def test():
    args=sys.argv
    print 'arguments:',args
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print  'Hello, %s!' %args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()


try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

def _private_1(name):#private
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):#public
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
