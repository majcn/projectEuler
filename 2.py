#!/usr/bin/python2
def fib(n):
    a,b = 0,1
    while a<n:
        while a%2==1:
            a,b = b,a+b
        yield a
        a,b = b,a+b

print sum(fib(4000000))
