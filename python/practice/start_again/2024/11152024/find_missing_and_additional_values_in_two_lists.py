#   https://www.geeksforgeeks.org/python-find-missing-additional-values-two-lists/


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
print ("Missing values in list1 ", set(list1).difference(list2))
print ("Additional values in list1 ", set(list2).difference(list1))

print ("Missing values in list2 ", set(list2).difference(list1))
print ("Additional values in list2 ", set(list1).difference(list2))