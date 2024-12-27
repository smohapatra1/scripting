#!/usr/bin/python
#Search and replace 
import re
string = "Python is Good"
result = re.sub(r'\G', "D",   string)
result2 = re.sub(r'\ ', "  ", string)
print (result)
print (result2)
