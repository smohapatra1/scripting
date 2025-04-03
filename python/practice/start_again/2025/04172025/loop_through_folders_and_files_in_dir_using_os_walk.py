#   https://www.geeksforgeeks.org/python-loop-through-folders-and-files-in-directory/

import os 
dir = 'test'
for path, folder, files in os.walk(dir):
    for filename in files:
        with open(os.path.join(dir, filename)) as f:
            print (f"Content of '{filename}'")
            print (f.read())
        print ()
    for folder_name in folder:
        print (f"Content of '{filename}")
        print (os.listdir(f"{path}/{folder_name}"))
        print ()
    break