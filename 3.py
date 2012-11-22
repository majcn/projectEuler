#!/usr/bin/python2
def primefactors(x):
    f = 1
    n = 2
    while n<=x:
        if x%n==0:
            x /= n
            f = n
        else:
            n += 1
    return f

print primefactors(600851475143)
