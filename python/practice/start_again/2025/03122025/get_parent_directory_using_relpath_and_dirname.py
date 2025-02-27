#   https://www.geeksforgeeks.org/get-parent-of-current-directory-using-python/

import os.path
def getParent(path, levels = 1 ):
    common = path
    for i in range(levels +1 ):
        common = os.path.dirname(common)
    return os.path.relpath(path, common)
path = '/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/file.txt'
print (getParent(path, 4))