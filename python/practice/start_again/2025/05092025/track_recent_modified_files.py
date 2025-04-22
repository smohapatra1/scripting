#   https://www.geeksforgeeks.org/python-create-archives-and-find-files-by-name/


import os 
import time
import sys
def modified_file(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.join(path, name)
                if mtime > (now - seconds):
                    print (fullpath)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ('Usage: {} dir seconds '.format(sys.argv[0]))
        raise SystemExit(1)
    modified_file(sys.argv[1], float(sys.argv[2]))
    