#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

from collections import deque

test_list = [4, 5, 7, 3, 10]
print ("The original list : ", str(test_list))
res = deque(test_list)
res.appendleft(13)
res.pop()
res = list(res)
print ("the list after append and remove : ", str(res))