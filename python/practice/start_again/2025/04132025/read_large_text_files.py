#   https://www.geeksforgeeks.org/how-to-read-large-text-files-in-python/

import fileinput
import time

start = time.time()
count = 0 
for lines in fileinput.input(['file.txt']):
    print (lines)
    count = count + 1
end = time.time()
print ("Execution in seconds: ", (end-start))
print ("No. of lines printed: ", count) 
