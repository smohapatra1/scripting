#   https://www.geeksforgeeks.org/how-to-save-file-with-file-name-from-user-using-python/


import pathlib
dir = 'test'
filepath = dir + input("Enter filename:")
pathlib.Path(filepath).touch()