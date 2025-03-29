#   https://www.geeksforgeeks.org/how-to-read-large-text-files-in-python/

import time 

start = time.time()
count = 0 
with open('file.txt') as f:
    for line in f:
        print (line)
        count = count +1 
end = time.time()
print ("Execution in seconds: ", (end-start))
print ("No of lines printed : ", count)