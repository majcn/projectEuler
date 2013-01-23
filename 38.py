#!/usr/bin/python2
for i in range(9123,9877):
    s = "".join([str(i*j) for j in range(1,3)])
    if len(s) == len(set(s)) and '0' not in s:
        res = s
print res
