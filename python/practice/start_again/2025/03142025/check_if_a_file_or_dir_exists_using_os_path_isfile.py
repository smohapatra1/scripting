#   https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/

import os 
dir = '/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/'
isExists = os.path.isfile(dir)
print (isExists)
file = '/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/file.txt'
isExists = os.path.isfile(file)
print (isExists)