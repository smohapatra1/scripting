#   https://www.geeksforgeeks.org/python-program-for-binary-search/

def BinarySearch(arr, low, high, x):
    if high >= low:
        mid  = (high + low )//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr, low, mid-1, x)
        else:
            return BinarySearch(arr, mid+1, high, x)
    else:
        return -1 
if __name__ == "__main__":
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
    res = BinarySearch(arr, 0 , len(arr)-1, x)
    if res != -1:
        print ("Element is present at index ", res)
    else:
        print ("Element is Not present in Array")
