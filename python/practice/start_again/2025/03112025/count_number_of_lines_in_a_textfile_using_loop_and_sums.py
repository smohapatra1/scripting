#   https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

with open('file.txt', 'r') as f:
    lines = sum(1 for line in f)
    print ("Total number of lines: ", lines)