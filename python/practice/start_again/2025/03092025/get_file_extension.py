#   https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/


import os 
split_up = os.path.splitext('file.txt')
print (split_up)
file = split_up[0]
file_ext = split_up[1]
print ("FileName : ", file)
print ("FileExtension : ", file_ext)