#!/usr/bin/python2
def get_primes_str(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(str(p))
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

sp = get_primes_str(1000000)
fsp = filter(lambda x: all(i not in x for i in ['0', '2', '4', '5', '6', '8']), sp)
fp = map(int, fsp)
print len(filter(lambda x: all(int(x[i:] + x[:i]) in fp for i in range(len(x))), fsp))+2