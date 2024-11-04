#   https://www.geeksforgeeks.org/python-difference-two-lists/

def Diff(list1, list2):
    # Solution -01
    # a = []
    # for i in list1:
    #     if i not in list2:
    #         a.append(i)
    # return a 
    # Solution - 02
    res = [val for val in list1 if val not in list2] 
    return res
    


if __name__ == "__main__":
    # list1 = [1, 2, 3, 4, 5, 6]
    # list2 = [4, 5, 6, 7, 8]
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print ("Diff between two lists : ", Diff(list1, list2))
