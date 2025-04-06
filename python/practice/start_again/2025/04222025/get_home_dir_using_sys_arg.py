#   https://www.geeksforgeeks.org/how-to-get-directory-of-current-script-in-python/

import sys
import os

print (os.path.dirname(sys.argv[0]))