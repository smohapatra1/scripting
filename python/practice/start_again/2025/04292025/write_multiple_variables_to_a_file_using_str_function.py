#   https://www.geeksforgeeks.org/write-multiple-variables-to-a-file-using-python/

a = "www.yahoo.com"
b = 2010
p = True
with open('file.txt', 'w') as f:
    f.write("Website name : " + str(a) + '\n')
    f.write("year         : " + str(b) + '\n')
    f.write("is popular   : " + str(p) + '\n')