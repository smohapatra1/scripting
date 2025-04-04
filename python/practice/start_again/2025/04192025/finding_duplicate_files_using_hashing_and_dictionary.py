#   https://www.geeksforgeeks.org/finding-duplicate-files-with-python/

import os 
import sys
from pathlib import Path
import hashlib

def findDuplicate(Subfolder):
    dup = {}
    for file_name in files:
        path = os.path.join(folders, file_name)
        file_hash = Hash_file(path)
        if file_hash in dup:
            dup[file_hash].append(file_name)
        else:
            dup[file_hash] = [file_name]
    return dup
def JoinDir(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
def Hash_file(path):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    blocksize = 65536
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()


dup = {} 
folders = Path('path/to/directory') 
files = sorted(os.listdir(folders)) 
for i in files: 
    JoinDir(dup, findDuplicate(i)) 
      
results = list(filter(lambda x: len(x) > 1, dup.values())) 
if len(results) > 0: 
    for result in results: 
        for sub_result in result: 
            print('\t\t%s' % sub_result) 
else: 
    print('No duplicates found.') 
