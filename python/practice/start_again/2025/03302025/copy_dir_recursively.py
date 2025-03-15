#   https://www.geeksforgeeks.org/copy-a-directory-recursively-using-python-with-examples/

import shutil

path = "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03302025"
src =  "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03302025"
dst = "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03302025/test/"
dest = shutil.copytree(src, dst)