#   https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/

from pathlib import Path

directory = 'files'

files = Path(directory).glob('*')
for file in files:
    print (file)