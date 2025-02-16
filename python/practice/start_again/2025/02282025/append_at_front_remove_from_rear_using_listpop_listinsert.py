#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

def append_front_remove_rear(test_list, front):
    test_list.pop()
    test_list.insert(0, front)
    return test_list

test_list = [4, 5, 7, 3, 10]
print ("Original list  :", test_list)
front = 13
print ("New list       :", append_front_remove_rear(test_list, front))