#   https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

import pathlib
empty_dir = 'test'
path = pathlib.Path(empty_dir).rmdir()
print ("Deleted '%s' successfully" % empty_dir)