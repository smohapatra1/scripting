#   https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

with open('file.txt', 'r') as f:
    for count, line in enumerate(f):
        pass
print ("Total lines are : ", count +1 )