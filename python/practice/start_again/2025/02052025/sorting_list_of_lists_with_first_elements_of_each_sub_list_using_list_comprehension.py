#   https://www.geeksforgeeks.org/sorting-list-of-lists-with-first-element-of-each-sub-list-in-python/

list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
print ("Original List : ", list_of_lists)
sorted_list = [ x for x in sorted(list_of_lists, key=lambda x:x[0])]
print ("New list      : ", sorted_list)



