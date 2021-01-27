#print date ane time 
from datetime import datetime 
now = datetime.now()
date = datetime.today()
print ("Date and Time - ", now)
print ("Date  - ", date.strftime("%d - %m - %y"))
print ("Date  - ", date.strftime("%B - %d - %y"))
print ("Date  - ", date.strftime("%b - %d - %y"))
print ("Time : ", now.strftime("%H - %M - %S"))