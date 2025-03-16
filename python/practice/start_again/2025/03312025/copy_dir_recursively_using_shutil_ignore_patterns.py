#   https://www.geeksforgeeks.org/copy-a-directory-recursively-using-python-with-examples/

import shutil

src = '2025/03312025'
dest = '2025/03312025/copy'
shutil.copytree(src, dest, ignore=shutil.ignore_patterns('file.txt'))