#!/usr/bin/python
#Regular expression
import re
pattern = re.compile("ello")
print (pattern.match("Hello World"))
print (pattern.match("Hello World", 1))
print (pattern.search("Hello World", 1))
print (pattern.search("Hello World", 2))
