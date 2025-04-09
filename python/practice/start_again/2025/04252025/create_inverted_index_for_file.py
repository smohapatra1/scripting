#   https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/

file = open('file.txt', encoding='utf8')
read = file.read()
file.seek(0)
read
line = 1
for word in read:
    if word == '\n':
        line += 1
print ("Number of lines in file is : ", line)
array = []
for i in range(line):
    array.append(file.readline())
array

