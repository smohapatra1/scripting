#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import os 

path = '/2025/03162025'

try:
    os.remove(path)
except OSError as error:
    print (error)
    print ("File path can not be removed")