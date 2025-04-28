#   https://www.geeksforgeeks.org/check-if-file-is-readable-in-python/

file_path = 'file.txt'
try:
    with open(file_path) as f:
        print ("File is readable")
except IOError:
    print ("File is not readable") 