#!/usr/bin/python2

res = 0
used = []
genNumbers = [i for i in range(1234,9877) if len(set(str(i))) == 4]
for i in genNumbers:
    for j in range(1, 1000):
        if i in used:
            continue
        if i%j != 0:
            continue
        s = str(i) + str(j) + str(i/j)
        if '0' in s:
            continue
        if len(set(s)) != 9 or len(s) != 9:
            continue
        res += i
        used.append(i)
print res
