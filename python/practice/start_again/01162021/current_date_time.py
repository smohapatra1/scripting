#print Current date and time 
from datetime import datetime

#print date
date = datetime.today()
print (date)
#Format-1
dt_str = date.strftime("%d-%m-%Y")
print (dt_str)
#format2
dt_str2 = date.strftime("%B-%d, %Y")
print (dt_str2)
#format3
dt_str3 = date.strftime("%b-%d, %Y")
time = datetime.now()
time_fmt1 = time.strftime("%H:%M:%S")
print ("%s and %s"  % (time, time_fmt1))
