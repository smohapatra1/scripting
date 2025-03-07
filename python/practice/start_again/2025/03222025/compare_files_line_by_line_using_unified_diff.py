#   https://www.geeksforgeeks.org/compare-two-files-line-by-line-in-python/

import difflib

with open('file1.txt') as f1:
    read1 = f1.readlines()
with open('file2.txt') as f2:
    read2 = f2.readlines()

for line in difflib.unified_diff(read1, read2, fromfile='file1.txt', tofile='file2.txt', lineterm=''):
    print (line)