#   https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/

import os 
dir = '2025'
isExists = os.path.isfile(dir)
print (isExists)
file = 'file.txt'
isExists = os.path.isfile(file)
print (isExists)