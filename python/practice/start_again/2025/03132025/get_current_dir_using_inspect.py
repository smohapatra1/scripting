#   https://www.geeksforgeeks.org/get-current-directory-python/


import inspect
import os
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print ("Current Dir : ", path)