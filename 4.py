#!/usr/bin/python2
import itertools as it
print max([x*y for x,y in it.product(range(1000), range(1000)) if str(x*y) == str(x*y)[::-1]])
