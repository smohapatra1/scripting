#   https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/


file = open('file.txt')
lines = [0, 3, 4]
for pos, l_num in enumerate(file):
    for pos in lines:
        print (l_num)
