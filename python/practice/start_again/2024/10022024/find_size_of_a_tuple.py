#   https://www.geeksforgeeks.org/find-the-size-of-a-tuple-in-python/

import sys

def Size(Tuple1, Tuple2, Tuple3):
    print ("Size of the Tuple1 is {} ".format(sys.getsizeof(Tuple1)))
    print ("Size of the Tuple2 is {} ".format(sys.getsizeof(Tuple2)))
    print ("Size of the Tuple3 is {} ".format(sys.getsizeof(Tuple3)))

if __name__ == "__main__":
    Tuple1 = ("A", 1, "B", 2, "C", 3)
    Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
    Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
    result = Size(Tuple1, Tuple2, Tuple3)