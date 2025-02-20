#   https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/

file = open('file.txt', 'r')
content = file.readlines()
print ("2nd line            : " , content[1])
print ("Print first 3 lines : " , content[0:3])
