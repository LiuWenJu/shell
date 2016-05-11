#!/usr/bin/env python
# encoding: utf-8

import sys

class A:
    s1 = 333
    __age = 0

    def __init__(self,age):
        self.__age=age
        return

    def __del__(self):
        print 'destroyed'
        return

    def __doSomething(self, s):
        print self.__age
        return

    def doSomething(self, s):
        self.__doSomething(s)
        print s

class AA(A):
    def doSomething(self, s):
        print '==='
        print s
        print '==='


def doSomething(v):
        vv=v+1
        return vv

def main():
    a=A(111)
    a.doSomething('222')
    print a.s1
    #del a
    aa=AA(111)
    aa.doSomething('222')
    #del aa
    print doSomething(444)
print '------------------------'

if __name__ == '__main__':
    main()
