#!/usr/bin/python2
from math import factorial
print sum([i for i in range(3,100000) if sum([factorial(x) for x in [int(k) for k in str(i)]]) == i])

#res = 0
#for i in range(3,100000):
#    t = [int(x) for x in str(i)]
#    s=sum([factorial(x) for x in t])
#    if i == s:
#        res += i
#print res

