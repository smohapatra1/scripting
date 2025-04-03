#   https://www.geeksforgeeks.org/python-loop-through-folders-and-files-in-directory/

import os 
dir = r"/test/"
for filename in os.scandir(dir):
    with open(os.path.join(dir, filename)) as f:
        print (f"Contents of '{filename}'")
        print (f.read())
    print ()