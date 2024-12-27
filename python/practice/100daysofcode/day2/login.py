#!/usr/bin/python
#If else for login user - if defined 

username = ("samar" , "saisha")
login = str(raw_input("What is your login name : "))
if login in username :
    print "Access granted"
else:
    print "Access Denied"

