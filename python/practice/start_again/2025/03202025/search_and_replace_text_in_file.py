#   https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

# Search file and replace without any module

import os 

search = 'dummy'
replace = 'replaced'
with open('file.txt', 'r') as f:
    data = f.read()
    data = data.replace(search, replace)
with open('file.txt', 'w') as f:
    f.write(data)

print ("Text Replaced")