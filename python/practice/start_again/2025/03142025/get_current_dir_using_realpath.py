#   https://www.geeksforgeeks.org/get-current-directory-python/

import os 
print ("File current location : ", os.getcwd())
print ("File location         :", os.path.realpath(os.path.dirname(__file__)))