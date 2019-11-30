#!/usr/bin/python
#Verify conditional statements
age = int(raw_input("Enter your age: "))
if ( age >= 40) :
    print "I am old"
elif ( age >=20 and age ==30):
    print "I am adult"
elif ( age >= 10 and age <= 18) :
    print "I am a teenager and %d years old" % age
elif ( age <=10 or age <=5 ):
    print "I am baby and %d year old" % age
    
