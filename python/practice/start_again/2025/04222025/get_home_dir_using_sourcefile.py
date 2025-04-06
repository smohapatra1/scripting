#   https://www.geeksforgeeks.org/how-to-get-directory-of-current-script-in-python/

from inspect import getsourcefile
import os
print (os.path.dirname(getsourcefile(lambda:0)))