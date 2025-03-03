#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import os 
dir = 'test'
location = '/2025/03162025/'
path = os.path.join(location, dir)
os.remove(path)
print ("%s has been removed successfully " % dir)