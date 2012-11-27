#!/usr/bin/python2
import itertools as it
print it.dropwhile(lambda n: any([n%i != 0 for i in range(11,20)]), it.count(20,20)).next()
