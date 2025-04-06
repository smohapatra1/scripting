#   https://www.geeksforgeeks.org/python-program-to-capitalize-the-first-letter-of-every-word-in-the-file/

file = open('file.txt', 'r')
print (file)

for line in file:
    output = line.title()
    print (output)