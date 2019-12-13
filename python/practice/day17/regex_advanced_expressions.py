#!/usr/bin/python
#Advacned regex expressions
import re
word= "Python is awesome"
result = re.search(r'(.*) is (.*?) .*', word, re.M|re.I)
print (result)
