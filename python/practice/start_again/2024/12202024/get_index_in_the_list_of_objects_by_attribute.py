#   https://www.geeksforgeeks.org/get-index-in-the-list-of-objects-by-attribute-in-python/


class X:
    def __init__(self, val):
        self.val = val 
    def getIndex(L, target):
        for index, x in enumerate(L):
            if x.val == target:
                return index
        return -1
L = [ 1, 2, 3, 4, 5, 6]
a = list()
for i in L :
    a.append(X(i))
print (getIndex(a, 3)) 


