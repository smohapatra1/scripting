#!/usr/bin/python
#break and continue statements
for char in "computer" :
    print (char)
print ("Ended the for loop")
#continue
for char in "computer" :
    if char == "p":
        #print (char)
        continue
    print ("Ended the continue loop - % s " %char )
#break
for char in "computer" :
    if char == "t" :
        #print (char)
        break
    print ("Ended the break loop - %s " %char)
