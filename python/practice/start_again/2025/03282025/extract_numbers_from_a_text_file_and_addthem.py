#   https://www.geeksforgeeks.org/extract-numbers-from-a-text-file-and-add-them-using-python/


h = open('file.txt', 'r')

lines = h.readlines()
 
a = 0 

for line in lines:
    for i in line:
        if i.isdigit() == True:
            a += int(i)
print ("The Sum is :", a )


