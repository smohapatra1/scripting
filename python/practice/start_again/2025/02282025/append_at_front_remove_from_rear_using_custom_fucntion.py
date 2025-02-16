#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

def append_front_remove_rear(test_list):
    test_list.insert(0, 13)
    test_list.pop()
    return test_list

test_list = [4, 5, 7, 3, 10]
print ("Original List : ", test_list)
res = append_front_remove_rear(test_list)
print ("New list      : ", res)
