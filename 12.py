#!/usr/bin/python2
from math import sqrt

n = 1
r = 0
while True:
    r += n
    n += 1
    c = sum([1 for i in range(1,int(sqrt(r))) if r%i == 0]) #problem when sqrt(r) == INT
    if c > 250:
        print r
        break
