#   https://www.geeksforgeeks.org/how-to-get-size-of-folder-using-python/

import os 
size = 0 

dir = 'test'
for ele in os.scandir(dir):
    size +=os.path.getsize(ele)
print (size)