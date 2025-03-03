#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import os 
dir = 'test'
parent = '/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03162025'
path = os.path.join(parent, dir)
os.rmdir(path)