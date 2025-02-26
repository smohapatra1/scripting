#   https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

with open('file.txt', 'r') as f:
    lines = len(f.readlines())
    print ("Total number of lines : ", lines)
