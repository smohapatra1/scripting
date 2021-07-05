
def BinarySearch (arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left +right )//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
arr = [1,2,3,4,5,6,9]
target = 5
result = BinarySearch(arr,target)
#print (result)
if result != 1 :
    print (f"Element {target} is present at index {result}")
else:
    print (f"Element {target} is not present in the array")