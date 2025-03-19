#   https://www.geeksforgeeks.org/python-program-to-replace-text-in-a-file/

import os

x = input("Enter texts to be replaced : ")
f = open('file.txt', 'r')
f1 = open('file2.txt', 'w')

f1.write(x)

os.remove('file.txt')
os.rename('file2.txt', 'file.txt')
f.close()
f1.close()
print("Data replaced successfully")