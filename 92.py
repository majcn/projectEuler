#!/usr/bin/python2
mem = {}
counter = 0
for x in range(2,10000000):
    arr = []
    while x != 1 and x != 89:
        arr.append(x)
        if x in mem:
            x = mem[x]
            break
        x = sum(int(i)**2 for i in str(x))
    counter += x == 89
    for i in arr:
        mem[i] = x
print counter