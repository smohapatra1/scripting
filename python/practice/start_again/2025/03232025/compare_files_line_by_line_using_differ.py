#   https://www.geeksforgeeks.org/compare-two-files-line-by-line-in-python/

from difflib import Differ

with open('file1.txt') as f1, open('file2.txt') as f2:
    differ = Differ()
    for line in differ.compare(f1.readlines(), f2.readlines()):
        print (line)