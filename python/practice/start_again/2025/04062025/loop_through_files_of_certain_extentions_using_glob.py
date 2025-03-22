#   https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/

import glob
for file in glob.glob('test\\**\\*.txt', recursive=True):
    print (file)