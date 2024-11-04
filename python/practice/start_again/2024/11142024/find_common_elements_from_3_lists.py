#       https://www.geeksforgeeks.org/python-program-find-common-elements-three-lists-using-sets/

def Common(arr1, arr2, arr3):
    # Solution -1 - Intersection Method
    # arr1_set = set(arr1)
    # arr2_set = set(arr2)
    # arr3_set = set(arr3)
    # s1 = arr1_set.intersection(arr2_set)
    # s2 = s1.intersection(arr3_set)
    # final = list(s2)
    # return s2

    # Solution -2 
    # common = set()
    # for item in arr1:
    #     if item in arr2 and item in arr3:
    #         common.add(item)
    # return common
    
    # Solution - 03 
    res = [item for item in arr1 if item in arr2 and item in arr3]
    return res


if __name__ == "__main__":
    # Elements in Array1
    arr1 = [1, 5, 10, 20, 40, 80, 100]
    # Elements in Array2
    arr2 = [6, 7, 20, 80, 100]
    # Elements in Array3
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    print ("Found common element and they are ", Common(arr1, arr2, arr3))