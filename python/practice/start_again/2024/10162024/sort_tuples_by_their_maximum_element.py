#   https://www.geeksforgeeks.org/python-program-to-sort-tuples-by-their-maximum-element/

test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
print ("Current list " + str(test_list))
test_list.sort(key = lambda sub: max(sub), reverse = True)
print ("Sorted list  " +str(test_list)) 