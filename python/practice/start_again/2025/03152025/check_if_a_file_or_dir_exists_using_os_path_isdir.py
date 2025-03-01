#   https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/

import os.path

dirname = "test"
os.mkdir(dirname)
symlink_path = "/03152025/"
os.symlink(dirname, symlink_path)
path = dirname
isdir = os.path.isdir(path)
print (isdir)
path = symlink_path
isdir = os.path.isdir(path)
print (isdir)
