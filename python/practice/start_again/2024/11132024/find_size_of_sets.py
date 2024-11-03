#   https://www.geeksforgeeks.org/find-the-size-of-a-set-in-python/
import sys

Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
print ("Size of the set1 : ", sys.getsizeof(Set1))
print ("Size of the set2 : ", sys.getsizeof(Set2))
print ("Size of the set3 : ", sys.getsizeof(Set3))
