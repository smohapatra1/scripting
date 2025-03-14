#   https://www.geeksforgeeks.org/python-check-if-a-directory-is-empty/

import os 

dir = 'test'
dir1 = os.listdir(dir)
if len(dir1) == 0 :
    print ("Directory is empty")
else:
    print ("Directory is not empty")