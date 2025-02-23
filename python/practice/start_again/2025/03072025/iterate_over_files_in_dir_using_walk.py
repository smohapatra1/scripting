#   https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/

import os 
directory = "files"
for root, dirs , files in os.walk(directory):
    for file in files:
        print (os.path.join(root, file))