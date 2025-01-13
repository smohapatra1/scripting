#   https://www.geeksforgeeks.org/python-program-for-linear-search/


def Linear_Search(arr, target, i=0):
    if i == len(arr):
        return -1 
    if arr[i] == target:
        return i 
    return Linear_Search(arr, target, i+1)

if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    target = 70
    result = Linear_Search(arr, target)
   
    if result != -1 :
        print ("Element is found at the Index ", result)
    else:
        print ("Element not found in the array")
    arr1 = [10, 23, 45, 70, 11, 15]
    target1 = 9
    result1 = Linear_Search(arr1, target1)
    if result1 != -1 :
        print ("Element is found at the Index ", result1)
    else:
        print ("Element not found in the array")