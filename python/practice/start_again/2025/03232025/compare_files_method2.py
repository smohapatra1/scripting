#   https://www.geeksforgeeks.org/how-to-compare-two-text-files-in-python/

f1 = open('file.txt', 'r')
f2 = open('file2.txt', 'r')

data1 = f1.readlines()
data2 = f2.readlines()
i = 0 
for line1 in data1:
    i += 1
    for line2 in data2:
        if line1 == line2:
            print ("Line ", i , ": IDENTICAL")
        else:
            print ("Line", i, ": DIFFERENT")
        break
f1.close() 
f2.close()