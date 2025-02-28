#   https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/

import os 
path = '2025'
isExist = os.path.exists(path)
print (isExist)
file = 'file1.txt'
isExist = os.path.exists(file)
print (isExist)