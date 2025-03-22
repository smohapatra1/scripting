#   https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/

import os 

dir ='test'
ext = ('ext', 'txt')

for path , dirc, files in os.walk(dir):
    for name in files:
        if name.endswith(ext):
            print (name)
