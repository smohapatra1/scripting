#   https://www.geeksforgeeks.org/how-to-save-file-with-file-name-from-user-using-python/

import os 

src = input("Enter src filename :")
dst = input("Enter dst filename :")

os.popen(f"copy {src} {dst}")