import datetime 
from datetime import date 
from datetime import datetime
#Print Date 
today = date.today()
print ("Today's Date is : ", today)
today = date.today()
today1 = today.strftime("%B %d, %Y")
print ("Today's Date in String Format : ", today1)
#Print Current Time 
timenow = datetime.now()
print ("Current time is : ", timenow)