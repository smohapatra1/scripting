#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import shutil
import os

dirs = '/test/test2/'

dir = 'test'
path = os.path.join(dirs, dir)
shutil.rmtree(path, ignore_errors=False)



