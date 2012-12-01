#!/usr/bin/python2
n = {
        0:"",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety",
        100:"hundred",
        1000:"thousand"
}

res = 0
for i in range(1,1001):
    if i in n:
        res += len(n[i]) if i<100 else len(n[i])+len(n[1])
    else:
        for k in [1000, 100]:
            t = i/k
            res += len(n[t])+len(n[k])+3 if t!=0 else 0
            i %= k
        x = len(n[i]) if i<=20 else len(n[i/10*10]) + len(n[i%10])
        res += x if x!=0 else -3
print res
