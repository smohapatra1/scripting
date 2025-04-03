
#   https://www.geeksforgeeks.org/python-loop-through-folders-and-files-in-directory/

import os 
import glob
dir = r"/test/"
for filename in glob.glob(f"{dir}/*"):
    with open(os.path.join(dir, filename)) as f:
        print (f"Content of '{filename}")
        print (f.read())
    print ()