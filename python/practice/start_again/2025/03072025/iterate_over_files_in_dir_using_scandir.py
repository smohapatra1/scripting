#   https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/

import os 

directory = "files"
for file in os.scandir(directory):
    if file.is_file():
        print (file.path)