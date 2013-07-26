#!/usr/bin/python2
from math import sqrt

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

N = 10000 #we assume that result is not higher then 10000

tas = [2*i*i for i in range(1,int(N/sqrt(N))/2)]
p = set(get_primes(N))
n = set(range(9,N,2)).difference(p)
goldbach = set(x+y for x in p for y in tas)
print min(n.difference(goldbach))