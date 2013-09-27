#!/usr/bin/python2
import re
roman_numbers = open('89.input').read()
print len(roman_numbers) - len(re.sub(r'DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII', '  ', roman_numbers))