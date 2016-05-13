#!/usr/bin/env python
# encoding: utf-8

while 1:
    try:
        x = raw_input("the first number:")
        y = raw_input("the second number:")

        r = float(x)/float(y)
        print r

    except Exception, e:
        print e
        print "try again."
    else:
        break



"""
this is a summary of try,except,else,finally's how to use

try:
    do something
except:
    do something
else:
    do something
finally:
    do something
"""
