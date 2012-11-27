#!/usr/bin/python2

def f():
    for a in xrange(1,1000):
        for b in xrange(1,1000):
            if (a+b)*1000 - a*b == 500000:
                return a*b*(1000-a-b)
print f()
