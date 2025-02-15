#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

test_list = [4, 5, 7, 3, 10]

print ("Original list : ", str(test_list))
res = [13] + [test_list[i] for i in range(len(test_list) - 1)]
print ("New list      : ", str(res))