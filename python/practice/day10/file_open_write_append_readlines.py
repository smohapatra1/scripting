#!/usr/bin/python
#Open a file write in it and append in it and read by lines
#Write
f=open("test.txt", "w+")
for i in range(10):
    f.write("Line %d\n" % (i+1))
#Append
f=open("test.txt", "a+")
for i in range(2):
    f.write("Appened new line %d \n" % (i+1))
#Read lines
f= open("test.txt", "r")
c= f.readlines()
i = 0 
for r in c:
    print ("Reading line %d - %s" % ((i+1), r))
    i = i + 1
