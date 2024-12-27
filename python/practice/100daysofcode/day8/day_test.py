#!/usr/bin/python
"""
## Using if statements, create a variable called day, set it to "Tuesday". Check to see if day is equal to "Monday" or "Tuesday", and if it is, print, "Today is sunny". If it is not, print "Today it will rain"
"""
day = "Tuesday"
edate = str(raw_input("Enter the day : "))
if (edate == day ):
  print ("Today is Sunny - %s ") % edate
else:
 print ("Today it will rain - %s ") % edate
