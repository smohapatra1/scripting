#   https://www.geeksforgeeks.org/python-program-for-bubble-sort/?ref=lbp

def bubble_sort(arr):
    for i in range(len(arr) -1, 0, -1):
        swap = False
        for n in range(i):
            if arr[n] > arr[n+1]:
                arr[n] , arr[n+1] = arr[n+1], arr[n]
                swap = True
        if not swap:
            break

if __name__ == "__main__":
    arr = [39, 12, 18, 85, 72, 10, 2, 18]
    print ("Unsorted Arrays ", arr)
    bubble_sort(arr)
    print ("After sorted    ", arr)