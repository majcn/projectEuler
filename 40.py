#!/usr/bin/python2
from operator import mul
d = [1, 10, 100, 1000, 10000, 100000, 1000000]
s = ""
stevec = 1
while len(s) < d[-1]:
    s += str(stevec)
    stevec += 1
print reduce(mul, [int(s[i-1]) for i in d], 1)