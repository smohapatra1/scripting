#   https://www.geeksforgeeks.org/how-to-remove-lines-starting-with-any-prefix-using-python/

file1 = open('file.txt', 'r')
file2 = open('file2.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('TextGenerators')):
        print (line)
        file2.write(line)
file2.close()
file1.close()