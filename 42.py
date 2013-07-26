#!/usr/bin/python2
from math import sqrt
def check(num):
    tmp = int(sqrt(num*2))
    return tmp*tmp+tmp == num*2

words = open('42.input').read().replace('"', '').split(',')
wordSums = [sum(map(lambda x: ord(x)-64, i)) for i in words]
print sum(map(check, wordSums))