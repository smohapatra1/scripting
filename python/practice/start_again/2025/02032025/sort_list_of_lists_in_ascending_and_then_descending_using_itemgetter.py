#   https://www.geeksforgeeks.org/sort-list-of-lists-ascending-and-then-descending-in-python/

from operator import itemgetter

a = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
print ("Orig : ", a )
a = sorted(a, key=itemgetter(0))
print ("Ascnd : ", a )
a = sorted(a, key=itemgetter(0), reverse=True)
print ("Decnd : ", a )