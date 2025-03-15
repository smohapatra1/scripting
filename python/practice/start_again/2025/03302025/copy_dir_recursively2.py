#   https://www.geeksforgeeks.org/copy-a-directory-recursively-using-python-with-examples/


import shutil
import os
import errno

src = "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03302025"
dst = "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03302025/test/"

try:
    shutil.copytree(src, dst)
except OSError as e:
    if e.errno == errno.ENOTDIR:
        shutil.copy(src, dst)
    else:
        print('Directory not copied. Error: %s' % e)