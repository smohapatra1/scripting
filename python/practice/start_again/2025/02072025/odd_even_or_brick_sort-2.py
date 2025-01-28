#   https://www.geeksforgeeks.org/python-program-for-odd-even-sort-brick-sort/

def oddEvenSort(arr, n ):
    isSorted = 0
    while isSorted == 0: 
        isSorted = 1
        arr[1::2], arr[2::2] = sorted(arr[1::2]), sorted(arr[2::2])
        for i in range(0, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0     
    return

if __name__ == "__main__":
    arr = [34, 2, 10, -9] 
    print ("Original : ", arr)
    n = len(arr) 
    oddEvenSort(arr, n); 
    print ("New One  : ", arr)