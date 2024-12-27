#Exercise Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
def thirdlist(x, y):
    listthree = list()
    odd1 = x[1::2]
    print (odd1)
    even1 = y [0::2]
    print (even1)
    listthree.extend(odd1)
    listthree.extend(even1)
    print(listthree)

#thirdlist(input("Enter first list with space and comma : "), input("Enter second list with spaces and comma :" ))
thirdlist([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])
