#   https://www.geeksforgeeks.org/python-program-for-selection-sort/?ref=lbp

def selectionsort(arr):
    l = len(arr)
    for i in range(l):
        min = i
        for j in range(i+1, l):
            if arr[j] < arr[min]:
                min = j 
            arr[i] , arr[min] = arr[min], arr[i]

if __name__ == "__main__":
    arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
    print ("Unsupported : ", arr)
    selectionsort(arr)
    print ("Sorted      : ", arr)