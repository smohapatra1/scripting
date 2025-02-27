#   https://www.geeksforgeeks.org/get-current-directory-python/

import os 
import sys
path = os.path.dirname(os.path.abspath(sys.argv[0]))
print ("Current Dir : ", path)