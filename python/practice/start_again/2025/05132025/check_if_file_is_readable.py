#   https://www.geeksforgeeks.org/check-if-file-is-readable-in-python/

import os 
file = 'file.txt'
if os.access(file, os.R_OK):
    print ("File is readable")
else:
    print ("File not readable")