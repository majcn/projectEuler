#!/usr/bin/python2
from itertools import product

a = [i**5 for i in range(10)]
oa = range(10)

res = 0
for i in product(oa, repeat=6):
    n = int(''.join(map(str,i)))
    res += n if n == sum(a[j] for j in i) else 0
print res-1
