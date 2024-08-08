#   Find the common elements between two lists.
list1 = [ 1, 2, 4, 5, 10]
list2 = [ 1, 2, 5, 11, 13, 15]
common_list = list(set(list1) & set(list2))
print (common_list)