#!/usr/bin/python2
a = range(2,101)
b = range(2,101)
print len(set(i**j for i in a for j in b))
