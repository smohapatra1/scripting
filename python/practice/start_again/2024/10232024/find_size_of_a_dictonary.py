#   https://www.geeksforgeeks.org/find-the-size-of-a-dictionary-in-python/

import sys
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print ("Size of Dict1 "+ str(sys.getsizeof(dic1)) + " bytes")
print ("Size of Dict2 "+ str(sys.getsizeof(dic2)) + " bytes")
print ("Size of Dict3 "+ str(sys.getsizeof(dic3)) + " bytes")
