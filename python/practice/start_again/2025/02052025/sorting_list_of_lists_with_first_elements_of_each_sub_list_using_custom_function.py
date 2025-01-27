#   https://www.geeksforgeeks.org/sorting-list-of-lists-with-first-element-of-each-sub-list-in-python/

def custom_sort(list_of_lists):
    return list_of_lists[0]

list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
print ("Original List : ", list_of_lists)
sorted_list = sorted(list_of_lists, key=custom_sort)
print ("Sorted List   : ", sorted_list)