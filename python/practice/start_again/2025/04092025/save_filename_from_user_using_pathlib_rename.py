#   https://www.geeksforgeeks.org/how-to-save-file-with-file-name-from-user-using-python/

import pathlib
import os 

src = input("Enter the source filename: ")
target = input("Enter target filename :")
pathlib(src).rename(target)

