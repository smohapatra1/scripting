#   https://www.geeksforgeeks.org/reading-binary-files-in-python/

with open('example.bin', 'rb') as f:
    print (f.tell())
    f.seek(10)
    print (f.tell())