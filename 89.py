#!/usr/bin/python2
roman_numbers = open('89.input').read()

mapper = zip(
    ('DCCCC', 'LXXXX', 'VIIII', 'CCCC', 'XXXX', 'IIII'),
    ('CM', 'XC', 'IX', 'CD', 'XL', 'IV')
)

nrn = roman_numbers
for i,d in mapper:
    nrn = nrn.replace(i, d)

print len(roman_numbers) - len(nrn)