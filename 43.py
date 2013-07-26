#!/usr/bin/python2
from itertools import permutations
def check(s):
    for i,d in enumerate([1,2,3,5,7,11,13,17]):
        if int(''.join(s[i:i+3]))%d != 0:
            return False
    return True

nums = [i for i in permutations("0123456789") if i[0] != '0']
print sum(int(''.join(i)) for i in filter(check, nums))