#Bubble sort 

def bubblesort(arr):
    n=len(arr)
    swapped=False
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped=True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return
arr=[10,11,1,2,1,5,6]
if __name__ == '__main__':
    #a=input("Enter the values with , ")
    #arr=a.split(',')
    bubblesort(arr)
    for i in range(len(arr)):
        print (" %s " %arr[i] , end="")
