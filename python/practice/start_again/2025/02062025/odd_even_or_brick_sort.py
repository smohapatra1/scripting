#   https://www.geeksforgeeks.org/python-program-for-odd-even-sort-brick-sort/

def oddEvenSort(arr, n ):
    sorted = 0 
    while sorted == 0:
        sorted = 1
        temp = 0 
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1], arr[i]
                sorted = 0 
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = 0 
    return 

if __name__ == "__main__":
    arr = [34, 2, 10, -9] 
    print ("Original : ", arr)
    n = len(arr) 
    oddEvenSort(arr, n); 
    print ("New One  : ", arr)