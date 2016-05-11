#!/usr/bin/env python
# encoding: utf-8

class Person(object):
    """
    THis is a test class.
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def color(self, color):
        print "%s's color is  %s"% (self.name, color)

    def doSomething(self):
        i = 1
        while i < 21:
            print i
            i += 1
        print "done!"

girl = Person("cangjingkong")
girl.color("white")
girl.doSomething()
