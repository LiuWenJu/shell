#!/usr/bin/env python
# encoding: utf-8

class ContextManagerOpenDemo(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print "String the Manager."
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *others):
        self.open_file.close()
        print "Exiting the Manager."

with ContextManagerOpenDemo("0513.txt", "r") as reader:
    print "In the Manager."
    for line in reader:
        print line
