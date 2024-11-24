#   https://www.geeksforgeeks.org/python-group-similar-elements-into-matrix/

from collections import Counter

test_list = [1, 3, 4, 4, 2, 3] 
temp = Counter(test_list)
res = [[key] * val for key, val in temp.items()]
print ("Current Values ", test_list)
print ("Final Values" , res)