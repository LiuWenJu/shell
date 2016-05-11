#!/usr/bin/env python
# encoding: utf-8
"""
当通过类来获取方法的时候，得到的是非绑定方法对象。
当通过实例获取方法的时候，得到的是绑定方法对象。
"""
class Foo(object):
    def bar(self):
        print "This is a normal method of class."


def main():
    f =Foo()
    return f.bar()



if __name__ == "__main__":
    main()



"""

"""
