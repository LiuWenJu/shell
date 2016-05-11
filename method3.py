#!/usr/bin/env python
# encoding: utf-8

T = 0

def check_t():
    #T = 3
    return T

class Foo(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        if check_t():
            return self.name
        else:
            return "no person"


if __name__ == "__main__":
    f = Foo("canglaoshi")
    name = f.get_name()
    print name
