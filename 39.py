#!/usr/bin/python2
#a = [(x,y,z) for x in range(1,999) for y in range(x,999) for z in range(y,999) if x+y+z < 999 and x*x + y*y == z*z] 

res = (0, 0)
for p in range(999):
    tmp = (p, 0)
    for x in range(1,p):
        for i in range(x,(p-x)/2):
            if x*x + i*i == (p-i-x)*(p-i-x):
                tmp = (p, tmp[1]+1)
    if res[1] < tmp[1]:
        res = tmp
print res[0]