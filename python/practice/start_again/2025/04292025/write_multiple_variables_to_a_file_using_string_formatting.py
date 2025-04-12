#   https://www.geeksforgeeks.org/write-multiple-variables-to-a-file-using-python/

a = "Websitename"
b = 2009
p = True

with open('file.txt', 'w') as f:
    f.write("Websitename : {}\n".format(a))
    f.write("year        : {}\n".format(b))
    f.write('Is popular  : {}\n'.format(p))