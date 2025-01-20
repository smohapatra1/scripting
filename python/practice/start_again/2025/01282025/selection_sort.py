#   https://www.geeksforgeeks.org/python-program-for-selection-sort/

def SelectionSort(arr, n ):
    for i in range(n):
        min_index = i 
        for j in range( i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
    n = len(arr)
    print ("Unsorted Arrays : ", arr)
    SelectionSort(arr, n )
    print ("Sorted Arrays   : ", arr)