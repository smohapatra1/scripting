#   https://www.geeksforgeeks.org/file-versioning-in-python/

import shutil
import os 
import datetime

def version_file(file_path):
    if os.path.exists(file_path):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        versioned_file = f"{file_path}.{timestamp}"
        shutil.copyfile(file_path, versioned_file)
        print (f"Version created : {versioned_file}")
    else:
        print ("File not found")

file_path = 'file.txt'
version_file(file_path)
