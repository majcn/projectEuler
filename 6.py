#!/usr/bin/python2
print sum(range(101))**2 - sum(map(lambda x: x*x, range(101)))
