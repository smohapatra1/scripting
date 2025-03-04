#   https://www.geeksforgeeks.org/reading-binary-files-in-python/

import os 

f = open('example.bin', 'rb')
try:
    bin=f.read()
    print (bin)
finally:
    f.close()