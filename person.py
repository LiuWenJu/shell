#!/usr/bin/env python
# encoding: utf-8

class Person(object):
    """
    This is a sample of class.
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def breast(self, n):
        self.breast = n

    def color(self, color):
        print "%s is %s "% (self.name, color)

    def how(self):
        print "%s's breast is %s "% (self.name, self.breast)


girl = Person("canglaoshi")
girl.breast(90)
girl.color("white")

girl.how()
