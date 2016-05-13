#!/usr/bin/env python
# encoding: utf-8

with open("0513.txt") as read_file, open("0513.txt", "w") as write_file:
    for line in read_file.readlines():
        write_file.write(line)

