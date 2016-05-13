#!/usr/bin/env python
# encoding: utf-8

class ContextManagerOpenDemo(object):

    def __enter__(self):
        print "Starting the Manager."

    def __exit__(self, *ohters):
        print "Exiting the Manager."


with ContextManagerOpenDemo():
    print "In the Manager."
