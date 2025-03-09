#   https://www.geeksforgeeks.org/how-to-compare-two-text-files-in-python/

import filecmp

d1 = '2025/03232025'
d2 = '2025/03242025'
files = ['file.txt']
match. mismatch, errors = filecmp.cmpfiles(d1, d2, files)
print ("Shallow comparison")
print ("Match", match)
print ("Mismatch", mismatch)
print ("Errors", errors)
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow=False)
print ("Deep comparison")
print ("Match", match)
print ("Mismatch", mismatch) 
print ("Errors", errors)