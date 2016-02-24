#coding: utf-8

class A():
   _aa = 1

   def __init__(self):
       # self.__aa = 0
       print 'hi, new class'

   def getAA(self):
       return self._aa

   def setAA(self, val):
       self._aa = val

if __name__ == '__main__':
   a = A()
   print a.getAA()
   a.setAA(5)
   print a.getAA()