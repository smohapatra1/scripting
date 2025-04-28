#   https://www.geeksforgeeks.org/check-if-file-is-readable-in-python/
import os 
file_path = 'file.txt'

if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
    print("File is readable")
else:
    print("File is not readable")