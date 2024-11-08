#   https://www.geeksforgeeks.org/python-intersection-two-lists/

def Intersection(lst1, lst2):
    # Solution - 01 
    # res = [val for val in lst1 if val in lst2]
    # return res
    # Solution - 02 
    return list(set(lst1) & set(lst2))


if __name__ == "__main__":
    lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
    lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
    print (Intersection(lst1, lst2))