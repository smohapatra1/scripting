#   https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

file = open('file.txt', 'r' )
counter = 0 
Content = file.read()
lines = Content.split('\n')
for i in lines:
    if i:
        counter +=1
print ("Number of lines are : ", counter)