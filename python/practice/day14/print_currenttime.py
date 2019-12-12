#!/usr/bin/python
#Print current time
import time
import datetime
import calendar
month= calendar.month(2050,1)
print (month)
time=datetime.datetime.now()
time2=time.strftime("%Y-%m-%d %H:%M:%S")
print (time)
print (time2)
