#!/usr/bin/env python
# encoding: utf-8

T = 1

class Foo(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def check_t():
        T = 1
        return T

    def get_name(self):
        if self.check_t():
            return self.name
        else:
            return "no person"


if __name__ == "__main__":
    f = Foo("canglaoshi")
    name = f.get_name()
    print name
