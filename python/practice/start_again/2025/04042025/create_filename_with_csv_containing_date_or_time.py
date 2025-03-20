#   https://www.geeksforgeeks.org/how-to-create-filename-containing-date-or-time-in-python/

from datetime import datetime

current_datetime = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
print ("Current date time = ", current_datetime)
filename = current_datetime+".csv"
file = open(filename, 'w')
print ("File created : ", file.name)
file.close()
