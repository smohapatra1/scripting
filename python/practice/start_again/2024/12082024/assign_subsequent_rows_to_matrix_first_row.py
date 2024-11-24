#   https://www.geeksforgeeks.org/python-assigning-subsequent-rows-to-matrix-first-row-elements/

test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
res = {test_list[0][ele] : test_list[ele+1] for ele in range(len(test_list)-1)}
print ("Original List : ", str(test_list))
print ("New list", str(res ))