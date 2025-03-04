#   https://www.geeksforgeeks.org/reading-binary-files-in-python/

size = 1024
with open('example.bin', 'rb') as f:
    while True:
        chunk = f.read(size)
        if not chunk:
            break
        print (chunk)

