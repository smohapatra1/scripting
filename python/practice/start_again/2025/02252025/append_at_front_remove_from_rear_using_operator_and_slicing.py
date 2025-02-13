#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/


test_list = [4, 5, 7, 3, 10]
print ("The Original list                 : " +str(test_list))
res = [13] + test_list[:-1]
print("The list after append and removal : "  + str(res))