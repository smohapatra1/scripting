#   https://www.geeksforgeeks.org/python-program-for-heap-sort/

def heapify(arr, n , i ):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = 1 
    if r < n and arr[largest] < arr[r]:
        largest = r 
    if largest != i :
        arr[i], arr[largest] = arr[largest] , arr[i]
        heapify(arr, n , largest) 

def HeapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i )
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0 )

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7, ]
    print ("Unsorted Array : ", arr)
    HeapSort(arr)
    print ("Sorted Array   : ", arr)