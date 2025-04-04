#   https://www.geeksforgeeks.org/finding-duplicate-files-with-python/

import os 
from pathlib import Path
from filecmp import cmp

data_dir = Path('test')
files = sorted(os.listdir(data_dir))
duplicateFiles = []
for file in files:
    dup1 = False
    for class_ in duplicateFiles:
        dup1 = cmp(data_dir/file, 
        data_dir/class_[0],
        shallow=False
        )
        if dup1:
            class_.append(file)
            break
    if not dup1:
        duplicateFiles.append([file])
print (duplicateFiles)


