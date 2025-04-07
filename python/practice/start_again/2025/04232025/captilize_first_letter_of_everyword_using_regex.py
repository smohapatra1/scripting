#   https://www.geeksforgeeks.org/python-program-to-capitalize-the-first-letter-of-every-word-in-the-file/

import re

def convert_to_uppercase(m):
    return m.group(1) + m.group(2).upper()

result = ""
file = open('file.txt', 'r')
for line in file:
    g = line.split()
    for elem in g:
        if len(result) > 0:
            result = result + re.sub("(^|\s)(\S)", convert_to_uppercase, elem) + " "
        else:
            result = re.sub("(^|\s)(\S)", convert_to_uppercase, elem)
print (result)

