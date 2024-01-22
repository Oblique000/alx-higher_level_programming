#!/usr/bin/python3

a = 89
b = 10
c = a
c, b, a = a, b, a
print("a={:d} - b={:d}".format(a, b))
