#   https://www.geeksforgeeks.org/problems/binary-search-1587115620/1
#   https://www.geeksforgeeks.org/python-program-for-binary-search/


def binary_search(arr, x ):
    low = 0 
    high = len(arr) - 1
    mid = 0 
    while low <= high:
        mid = (high +low )//2
        if arr[mid] < x:
            low = mid +1 
        elif arr[mid] > x:
            high = mid - 1 
        else:
            return mid
    return -1 
if __name__ == "__main__":
    arr = [ 2, 3, 4, 10, 40, 50 ]
    x = 50
    result = binary_search(arr, x)
    if result != -1:
        print ("Element is present at index", result)
    else:
        print ("Element is not present in the array")