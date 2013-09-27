#!/usr/bin/python2
from fractions import Fraction
print sum(map(int, str(reduce(lambda x,y: y+Fraction(1, x), reversed([2] + sum([[1, i*2, 1] for i in range(1,34)], []))).numerator)))
