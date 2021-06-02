#Binary Search

def BinarySearch(arr, target):
    left = 0 
    right = len(arr) - 1
    while left <= right:
        mid = (left + right )//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            left = mid + 1
        else:
            right = mid +1 
    #return -1  
arr = [100,2000,3, 4, 5 ]
target = 5 
result = BinarySearch(arr,target)
print (result)