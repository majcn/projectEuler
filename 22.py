#!/usr/bin/python2
f = sorted(open('22.input').readline().replace('"', '').split(","))
print sum([reduce(lambda x,y: x+ord(y)-64, d, 0)*(i+1) for i,d in enumerate(f)])
