#   https://www.geeksforgeeks.org/python-program-to-capitalize-the-first-letter-of-every-word-in-the-file/

import string

result = ""
file = open('file.txt', 'r')
for line in file:
    g = line.split()
    for elem in g:
        if len(result) > 0:
            result = result + " " + string.capwords(elem)
        else:
            result = string.capwords(elem)
print (result)