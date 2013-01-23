#!/usr/bin/python2
print sum([i for i in range(1,1000000) if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]])
