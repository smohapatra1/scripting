#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import os
dir = '/test/test2/'

for filename in os.listdir(dir):
    filepath = os.path.join(dir, filename)
    if os.path.isfile(filepath):
        print (f"Found file   : {filename}")
        os.remove(filepath)
        print (f"Deleted file : {filename}")