#   https://www.geeksforgeeks.org/remove-multiple-elements-from-a-list-in-python/


def RemMultiple(n):
    # Solution 1 
    # list1 = [ ele for ele in n if ele % 2 != 0 ]
    # print ("Removed even numbers from list and new list is -  ", *list1)

    # Solution 2 
    rem = [ 1, 5 ]
    list1 = [ ele for ele in n if ele not in rem]
    print ("Removed numbers from list and new list is -  ", *list1)

if __name__ == "__main__":
    n = [ 1, 5, 12, 13, 14]
    result = RemMultiple(n)