#   https://www.geeksforgeeks.org/python-check-two-lists-least-one-element-common/

def Common(a,b):
    # Solution - 01 
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False

    # Solution - 02 
    # a_set = set(a)
    # b_set = set(b)
    # if len(a_set.intersection(b_set)) > 0:
    #     return True
    # else:
    #     return False


if __name__ == "__main__":
    # a = [1, 2, 3, 4, 5]
    # b = [5, 6, 7, 8, 9]
    
    a =[1, 2, 3, 4, 5]
    b =[6, 7, 8, 9]
    print ("Finding the common elements: ", Common(a, b ))