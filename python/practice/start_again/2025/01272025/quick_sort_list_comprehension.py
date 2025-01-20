#   https://www.geeksforgeeks.org/python-program-for-quicksort/

def quicksort(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr[0]
        left = [ x for x in arr[1:] if x < pivot]
        right = [ x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    arr = [1, 7, 4, 1, 10, 9, -2]
    print ("Unsorted array : ", arr)
    arr = quicksort(arr)
    print ("Sorted array   : ", arr)