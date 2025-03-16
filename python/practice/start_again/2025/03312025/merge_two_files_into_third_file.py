#   https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/

data = data2 = ""

with open('file.txt') as f1:
    data = f1.read()
with open('file2.txt') as f2:
    data2 = f2.read()

data += "\n"
data2 += data2

with open('file3.txt', 'w') as f3:
    f3.write(data)
    f3.write(data2)
f3.close()
