#   https://www.geeksforgeeks.org/copy-a-directory-recursively-using-python-with-examples/

import shutil

def ignore_function(file):
    def _ignore_(path, names):
        ignored = []
        if file in names:
            ignored.append(file)
        return set(ignored)
    return _ignore_

src = '2025/03312025'
dest = '2025/03312025/copy'
shutil.copytree(src, dest, ignore=ignore_function('file.txt'))
