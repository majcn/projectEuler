#!/usr/bin/python2
import datetime

def genDates():
    d = datetime.date(1901, 1, 6)
    while d < datetime.date(2001, 1, 1):
        yield d
        d += datetime.timedelta(days=7)

print sum([1 for i in genDates() if i.day == 1])
