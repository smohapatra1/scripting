#   https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/

import os 
directory = "files"
for files in os.listdir(directory):
    f = os.path.join(directory, files)
    if os.path.isfile(f):
        print (f)