#   https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

import shutil


shutil.copy(src, dst)
shutil.copy2(src, dst)
shutil.copytree(src, dst)
shutil.move(src, dst)