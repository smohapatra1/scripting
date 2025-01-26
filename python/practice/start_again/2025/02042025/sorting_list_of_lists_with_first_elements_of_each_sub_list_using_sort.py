#   https://www.geeksforgeeks.org/sorting-list-of-lists-with-first-element-of-each-sub-list-in-python/

list_of_lists= [[3, 'b'], [1, 'a'], [2, 'c']]
print ("Original :", list_of_lists)
list_of_lists.sort(key=lambda x:x[0])
print ("Sorted   :", list_of_lists)