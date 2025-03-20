#   https://www.geeksforgeeks.org/how-to-create-filename-containing-date-or-time-in-python/

from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print ("Current date and time : ", current_datetime)
str_current_datetime = str(current_datetime)
file_name = str_current_datetime+".txt"
file = open(file_name, "w")
print ("File created : ", file_name)
file.close()
