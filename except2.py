#!/usr/bin/env python
# encoding: utf-8

class Calculator(object):
    is_raise = True
    def calc(self, express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                print "zero can not be division."
            else:
                raise

if __name__ == "__main__":
    c = Calculator()
    print c.calc("8/0")
