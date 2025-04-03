#   https://www.geeksforgeeks.org/python-loop-through-folders-and-files-in-directory/


import os 

dir = "test"

for name in os.listdir(dir):
    with open(os.path.join(dir, name)) as f:
        print (f"Contents of '{name}'")
        print(f.read())
    print ()