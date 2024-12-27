#!/usr/bin/python
a = 0 
while a < 2 :
    b = raw_input ("Enter a multiple lists with commmand separated  - %s : " % a )
    c = b.split(",")
    d = list(c)
    listnum = len(d)
    #print ("Number of lists are - %s" %listnum)
    print ("%s: %s" % (a, d))
    a +=1
    while listnum == 1:
        del d[-1]
        print (d[-1])
    #for i in d:
    #    print (i)


