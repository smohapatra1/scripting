#   https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/

from pathlib import Path

path = "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03152025"

obj = Path(path)
print (obj.exists())