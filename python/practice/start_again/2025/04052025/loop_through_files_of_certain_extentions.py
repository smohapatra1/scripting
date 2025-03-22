#   https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/

import os 

dir = "test"

ext = ('.exe', '.txt')

for files in os.listdir(dir):
    if files.endswith(ext):
        print (files)
    else:
        continue