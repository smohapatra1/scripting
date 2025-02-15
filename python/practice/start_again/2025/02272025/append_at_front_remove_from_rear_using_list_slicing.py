#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

def append_front_remove(test_list, front):
    return [front] + test_list[:-1]

test_list = [4, 5, 7, 3, 10]
print ("Original list : ", test_list)
front = 13 
print ("New list      : ", append_front_remove(test_list, front))