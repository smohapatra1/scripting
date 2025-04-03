#   https://www.geeksforgeeks.org/python-loop-through-folders-and-files-in-directory/

import os 
from pathlib import Path

dir = "test"

files = Path(dir).glob("*")
for filename in files:
    with open(os.path.join(dir, filename)) as f:
        print (f"Contents for '{filename}'")
        print (f.read())
    print ()