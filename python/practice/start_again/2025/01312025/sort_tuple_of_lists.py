#   https://www.geeksforgeeks.org/sort-tuple-of-lists-in-python/

tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])
print ("Unsorted Tuples : ", tuple_of_lists)
sorted_tuple = tuple(sorted(sublist) for sublist in tuple_of_lists)
print ("Sorted Tuples   : ", sorted_tuple)
