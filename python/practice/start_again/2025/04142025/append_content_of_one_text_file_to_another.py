#   https://www.geeksforgeeks.org/python-append-content-of-one-text-file-to-another/

f1 = open('file.txt', 'r')
f2 = open('file3.txt', 'r')

print ("Content of first file  - ", f1.read())
print ("Content of second file - ", f2.read())
f1.close()
f2.close()
f1 = open('file.txt', 'a+')
f2 = open('file3.txt', 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)
print ("Content of first file  - ", f1.read())
print ("Content of second file - ", f2.read())

f1.close()
f2.close()

