#!/usr/bin/python2
def hexagonal(n):
    while True:
        yield n*(2*n-1)
        n += 1

def pentagonal(n):
    while True:
        yield n*(3*n-1)/2
        n += 1

def triangle(n):
    while True:
        yield n*(n+1)/2
        n += 1

gen = [triangle(286), pentagonal(166), hexagonal(144)]
d = map(lambda x: x.next(), gen)
while len(set(d)) > 1:
    m = d.index(min(d))
    d[m] = gen[m].next()
print d[0]