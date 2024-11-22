#   https://www.geeksforgeeks.org/find-the-size-of-a-tuple-in-python/

import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
print ("Size of the Tuple1 is : ", str(sys.getsizeof(Tuple1)) + " bytes")
print ("Size of the Tuple2 is : ", str(sys.getsizeof(Tuple2)) + " bytes")
print ("Size of the Tuple3 is : ", str(sys.getsizeof(Tuple3)) + " bytes")