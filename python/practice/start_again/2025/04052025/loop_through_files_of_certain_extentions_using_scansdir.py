#   https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/
import os 

dir = 'test'
ext = ('.exe', 'txt')

for files in os.scandir(dir):
    if files.path.endswith(ext):
        print (files)
    else:
        continue