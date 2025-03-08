#   https://www.geeksforgeeks.org/how-to-compare-two-text-files-in-python/

import filecmp
f1 = 'file.txt'
f2 = 'file2.txt'
result = filecmp.cmp(f1, f2)
print (result)
result = filecmp.cmp(f1, f2, shallow=False)
print (result)