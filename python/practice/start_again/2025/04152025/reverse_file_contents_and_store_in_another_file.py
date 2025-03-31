#   https://www.geeksforgeeks.org/python-program-to-reverse-the-content-of-a-file-and-store-it-in-another-file/

f1 = open('file2.txt', 'w')
with open('file.txt', 'r') as f:
    data = f.read()
data1 = data[::-1]
f1.write(data1)
print ("Words reversed and written in a new file")
f1.close()
