#   https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/

import pathlib
file_ext = pathlib.Path('file.txt').suffix
print ("File Extension : ", file_ext)