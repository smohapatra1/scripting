#   https://www.geeksforgeeks.org/sort-list-of-lists-ascending-and-then-descending-in-python/

from functools import cmp_to_key

a = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
print ("Original :", a)

def compare(x, y):
    return x[0] - y[0]

asc = sorted(a, key=cmp_to_key(compare))
print ("Ascn     :", asc)
dsc = sorted(a, key=cmp_to_key(compare), reverse=True)
print ("Dsnd     :", dsc)

