#   https://www.geeksforgeeks.org/python-program-to-replace-text-in-a-file/

import sys
import fileinput

x = input("Enter texts to be replaced : ")
y = input("Enter texts that will replace : ")

for l in fileinput.input(files = 'file.txt'):
    l = l.replace(x, y)
    sys.stdout.write(l)