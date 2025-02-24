#   https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/#main

import glob

directory = 'files'
for file in glob.iglob(f'{directory}/*'):
    print (file)