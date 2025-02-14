#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

from itertools import islice

test_list = [4, 5, 7, 3, 10]
print ("The original list : ", test_list)
res = [13] + list(islice(test_list, 0, len(test_list) - 1))
print ("The list after append and remove : ", str(test_list))