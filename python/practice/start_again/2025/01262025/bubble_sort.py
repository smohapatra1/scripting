#   https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def BubbleSort(arr):
    for n in range(len(arr)-1, 0, -1):
        swap = False
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        if not swap:
            break

if __name__ == "__main__":
    arr = [39, 12, 18, 85, 72, 10, 2, 18]
    print ("Unsorted : ", arr)
    BubbleSort(arr)
    print ("Sorted :   ", arr)