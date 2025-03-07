#   https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/

import os

count = 0
with open('file.txt', 'r') as f:
    data = f.read()
    lines = data.split(' ')
    count +=len(lines)
print ("Number of words are : ", count)