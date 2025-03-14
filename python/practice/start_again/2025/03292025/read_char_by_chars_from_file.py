#   https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/

file = open('file.txt', 'r')

while 1:
    char = file.read(1)
    if not char:
        break
    print (char, end='')
file.close()