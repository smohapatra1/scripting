#   https://www.geeksforgeeks.org/sort-tuple-of-lists-in-python/

tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])
print ("Unsorted Tuple : ", tuple_of_lists)
sorted_tuple=tuple([*map(int, sorted(sublist))] for sublist in tuple_of_lists)
print ("Sorted Tuple   : ", sorted_tuple)