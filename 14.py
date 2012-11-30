#!/usr/bin/python2

import operator

cache = {}
for i in xrange(1,1000000):
    n = i
    c = 0
    while n != 1:
        if n in cache:
            c += cache[n]
            break
        n = n/2 if n%2==0 else 3*n+1
        c += 1
    cache[i] = c

print max(cache.iteritems(), key=operator.itemgetter(1))[0]
