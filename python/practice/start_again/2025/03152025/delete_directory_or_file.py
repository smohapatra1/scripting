#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import os
dirname = 'test'
os.mkdir(dirname)
file = 'file1.txt'
location = '03152025'
path = os.path.join(location, file)
os.remove(path)
