#!/usr/bin/env python
# encoding: utf-8

class Fraction(object):
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + '/' + str(self.denom)

    __repr__ = __str__

if __name__ == "__main__":
    a = int(raw_input("Please input a number: "))
    b = int(raw_input("Please input another number: "))
    f = Fraction(a, b)
    print "The fraction is ",f


