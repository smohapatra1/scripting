#!/usr/bin/python
#Convert seconds to day,hour,minutes,seconsds
a = int(input("Enter the seconds value : "))
day = a / ( 24 * 3600 )
hour = (a % ( 24 * 3600)) // 3600
minutes = (a % 3600) // 60
seconds = a % 60
print ("%d days %d hours %d minutes %d seconds" % (day, hour, minutes, seconds))  
