#   https://www.geeksforgeeks.org/sort-tuple-of-lists-in-python/

tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])
print ("unsorted list : ", tuple_of_lists)
sorted_tuple = tuple(map(sorted, tuple_of_lists))
print ("Sorted list   : ", sorted_tuple)