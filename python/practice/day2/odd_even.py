#!/usr/bin/python

# Print if number is ODD or Even


a = int(raw_input("Enter a number: "))
if  ( a % 2 ) == 0 : 
    print("%d is an even number" % a )
elif ( a / 4 ) == 0 :
    print ("%d is multiplied by 4" % a)
else:
    print("%d is an odd number" % a )

