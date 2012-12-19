#!/usr/bin/python2
import itertools

c = 0
for i in itertools.permutations('0123456789'):
    c+=1
    if c == 1000000:
        print ''.join(i)
        break
