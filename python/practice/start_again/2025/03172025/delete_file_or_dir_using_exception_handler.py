#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import shutil
import os 
def handler(func, path, exec_info ):
    print ("Inside Handler ")
    print (exec_info)

dirs = '/test/test2/'

dir = 'test'
path = os.path.join(dirs, dir)
shutil.rmtree(path, onerror=handler)