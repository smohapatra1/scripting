#   https://www.geeksforgeeks.org/reading-binary-files-in-python/

import pickle

with open('example.bin', 'rb') as f:
    data = pickle.load(f)
    print (data)