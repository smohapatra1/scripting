#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

test_list = [4, 5, 7, 3, 10]
print ("The original list : ", str(test_list))
test_list.pop()
test_list.insert(0, 13)
print ("The list after append and removal ", str(test_list))
