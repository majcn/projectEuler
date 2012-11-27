#!/usr/bin/python2
def gen_primes(th):
    D = {}
    q = 2
    counter = 1
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            [D.setdefault(p+q, []).append(p) for p in D[q]]
            del D[q]
        q+=1
        if q > th:
            break

print sum([i for i in gen_primes(2000000)])
