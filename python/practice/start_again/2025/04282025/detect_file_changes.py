#   https://www.geeksforgeeks.org/how-to-detect-file-changes-using-python/

import os 
import time 

def detect_file_changes(file_path, interval = 1):
    changed = os.path.getatime(file_path)
    while True:
        current_modified = os.path.getatime(file_path)
        if current_modified != changed:
            print ("File has changed")
            changed = current_modified
        time.sleep(interval)
detect_file_changes('file.txt')