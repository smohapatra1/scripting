#   https://www.geeksforgeeks.org/how-to-get-size-of-folder-using-python/

import os 
size = 0
path = 'test'
for path, dirs, files in os.walk(path):
    for f in files:
        fp = os.path.join(path, f)
        size +=os.path.getsize(fp)
print ("Folder path is : ", size)