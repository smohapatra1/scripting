#   https://www.geeksforgeeks.org/how-to-get-size-of-folder-using-python/

import os 
size = 0 
dir = 'test'
for path, dirs, files in os.walk(dir):
    for f in files:
        fp = os.path.join(path, f)
        size += os.stat(fp).st_size
print ('Folder size: ' + str(size))