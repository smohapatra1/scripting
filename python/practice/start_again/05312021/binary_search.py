#Program to do Binary Search 
#Start and end pointers

def binarySearch(arr, target):
    left = 0 
    right = len(arr) - 1 
    while (left <= right):
        mid = (left + right) //2 
        if( arr[mid] == target ):
            return mid
        elif (arr[mid] < target ):
            left = mid + 1
        else:
            right = mid -1
    return - 1 

arr = [1, 2,3, 4, 5, 6,7,8,9,10,11,12,12 ]
target = 11
result = binarySearch(arr, target)

if result != -1:
    print (f"Element is present at index {result}")
else:
    print (f"Element is not present at index")

