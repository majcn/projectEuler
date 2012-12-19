#!/usr/bin/python2

res = []
for i in range(1,1000):
    b = 10*(1%i)
    bo = [b]
    while b!=0:
        b = 10*(b%i)
        if b in bo:
            res.append((len(bo)-bo.index(b),i))
            break
        bo.append(b)

print max(res)[1]
