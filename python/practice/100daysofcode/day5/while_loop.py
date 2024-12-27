#!/usr/bin/python
#While loop
c = int(raw_input("Enter a number:  "))
while c <=5 :
    print (c)
    c = c + 1
#Continue
while c <= 5 :
    c = c+1
    print ("Printing - continue %d") %c
    if c==4 :
        continue
        c=c+1
    print (c)
#Break
while c <= 10:
    print ("printing - break %d") %c
    if c == 3 :
        break
    c = c+1
    print (c)
#Pass
while c <= 5:
    c = c+1 
    if c == 3 :
        pass
    print (c)

