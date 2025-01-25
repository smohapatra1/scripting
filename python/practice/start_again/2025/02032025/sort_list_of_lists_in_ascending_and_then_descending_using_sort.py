#   https://www.geeksforgeeks.org/sort-list-of-lists-ascending-and-then-descending-in-python/

a = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
print ("Orig : ", a)
a.sort(key=lambda x: x[0])
print ("Asnd : ", a)
a.sort(key=lambda x:x[0], reverse=True)
print ("Dcnd : ", a)