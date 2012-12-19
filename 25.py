#!/usr/bin/python2
c, a, b = 1, 1, 1
while len(str(a)) != 1000:
    c, a, b = c+1, b, a+b
print c
