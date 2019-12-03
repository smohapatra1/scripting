#!/usr/bin/python
#Print numbers from 1-100
counter = 0
while counter < 100 :
    print ("Counter % d") % counter
    counter = counter + 1

#Then print only 4 numbers out of 100
counter = 0 
while counter < 100:
    print ("Counter 4 %d") % counter
    counter = counter + 1
    if counter == 4 :
        break
    else:
        pass

#Continue statements - It just bypass the term which is matching
i = 0 
for i in range(1,10):
    if i == 4:
        continue
    print (i)
