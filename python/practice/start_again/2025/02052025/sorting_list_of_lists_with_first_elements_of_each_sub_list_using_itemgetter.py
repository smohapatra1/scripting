#   https://www.geeksforgeeks.org/sorting-list-of-lists-with-first-element-of-each-sub-list-in-python/

from operator import itemgetter

list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
print ("Original List : ", list_of_lists)
sorted_list = sorted(list_of_lists, key=itemgetter(0))
print ("Sorted List   : ", sorted_list)