#!/usr/bin/env python
# encoding: utf-8

while 1:
    print "this is a division program."
    c = raw_input("input 'c' contnue, otherwise logout:")
    if c == 'c':
        a = raw_input("first number:")
        b = raw_input("second number:")
        try:
            print float(a)/float(b)
            print "*"*30

        except ZeroDivisionError:
            print "The second number can't be division."
            print "*"*30
        except ValueError:
            print "please input number."
            print "*"*30

    else:
        break
