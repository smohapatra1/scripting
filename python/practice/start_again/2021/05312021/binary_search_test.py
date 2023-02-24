#Binary Search test 

def BinarySearch(arr, p):
    left = 0 
    right = len(arr) - 1
    while left <= right:
        mid = (left +right) //2
        if arr[mid] == p:
            return mid
        elif arr[mid] < p:
            left = mid +1 
        else:
            right = mid -1
    return -1

arr = [1,2,3,4,5,6]
p = 4
result = BinarySearch(arr,p)
print (result)
