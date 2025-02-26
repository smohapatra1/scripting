#   https://www.geeksforgeeks.org/python-program-to-read-file-word-by-word/

with open('file.txt', 'r') as f:
    for line in f:
        for word in line.split('\n'):
            print (word)