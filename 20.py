#!/usr/bin/python2
from operator import mul
print sum([int(i) for i in str(reduce(mul, range(1,101)))])
