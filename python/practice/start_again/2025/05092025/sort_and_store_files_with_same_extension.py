#   https://www.geeksforgeeks.org/python-sort-and-store-files-with-same-extension/

import os 
import shutil

path = 'test'
list = os.listdir(path)
for file in list:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

