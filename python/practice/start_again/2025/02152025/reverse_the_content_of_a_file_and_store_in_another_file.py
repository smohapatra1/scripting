#   https://www.geeksforgeeks.org/python-program-to-reverse-the-content-of-a-file-and-store-it-in-another-file/

f1 = open("output1.txt", "w")
with open("file.txt", "r") as myfile:
    data = myfile.read()

data1 = data[::-1]
f1.write(data1)
f1.close() 