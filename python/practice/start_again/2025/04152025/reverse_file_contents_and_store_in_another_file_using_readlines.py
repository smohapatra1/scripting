#   https://www.geeksforgeeks.org/python-program-to-reverse-the-content-of-a-file-and-store-it-in-another-file/

f1 = open('file2.txt', 'w')
with open('file.txt', 'r') as f:
    data=f.readlines()
data1 = data[::-1]
f1.writelines(data1)
f1.close()
print ("Words revered and written into a new file")