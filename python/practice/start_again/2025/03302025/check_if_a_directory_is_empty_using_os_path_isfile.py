#   https://www.geeksforgeeks.org/python-check-if-a-directory-is-empty/

import os
def isEmpty(path):
    if os.path.exists(path) and not os.path.isfile(path):
        if not os.listdir(path):
            print ("Empty Directory")
        else:
            print ("Not Empty Directory")
    else:
        print ("The path is either for a file or doesn't exist")

if __name__ == "__main__":
    path = 'test'
    isEmpty(path)
    print ()
    path = 'file.txt'
    isEmpty(path)
    print ()