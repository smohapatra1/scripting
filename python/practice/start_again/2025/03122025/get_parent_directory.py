#   https://www.geeksforgeeks.org/get-parent-of-current-directory-using-python/

import os 
path = os.getcwd()
print ("Current Dir : ", path)
print ("Parent Dir  : ", os.path.abspath(os.path.join(path, os.pardir)))