#Run the functions and examine stack trace.
import traceback
values = [ 1, 2, 3, 4]
try:
    value = values[5]
except:
    traceback.print_exc()
print ("End of program")