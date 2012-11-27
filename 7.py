#!/usr/bin/python2
def gen_primes(n):
    D = {}
    q = 2
    counter = 1
    while True:
        if q not in D:
            yield q
            if counter >= n:
                break
            else:
                counter += 1
            D[q*q] = [q]
        else:
            [D.setdefault(p+q, []).append(p) for p in D[q]]
            del D[q]
        q+=1

print [i for i in gen_primes(10001)][-1]
