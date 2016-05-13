#!/usr/bin/env python
# encoding: utf-8

read_file = open("0513.txt")
write_file = open("0513.txt", "w")

try:
    r = read_file.readlines()
    for line in r:
        write_file.write(line)

finally:
    read_file.close()
    write_file.close()
