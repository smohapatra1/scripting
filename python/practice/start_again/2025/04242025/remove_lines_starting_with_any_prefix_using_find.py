#   https://www.geeksforgeeks.org/how-to-remove-lines-starting-with-any-prefix-using-python/

file1 = open('file.txt', 'r')
file2 = open('file2.txt', 'w')

for line in file1.readlines():
    if not (line.find('line')==0):
        print (line)
        file2.write(line)
file1.close()
file2.close()