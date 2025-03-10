#   https://www.geeksforgeeks.org/reading-and-writing-lists-to-a-file-in-python/

L = ["Geeks\n", "for\n", "Geeks\n"]

file1 = open('file.txt', 'w')
file1.writelines(L)
file1.close()
print ('File written successfully')