
def bubblesort(arr):
    swapped=False
    n=len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped=True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return
if __name__ == '__main__':
    items=input("Enter the number of arrays with , : ")
    arr=items.split(',')
    #arr=[ 64, 34, 25, 12, 22, 11, 90 ]
    bubblesort(arr)
    for i in range(len(arr)):
        print (" %s " % arr[i], end=" ")