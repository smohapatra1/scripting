#   How would you implement the insertion sort algorithm?


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1 
        k = arr[i]
        while ( j >= 0) and (arr[j] > k ):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
        
if __name__ == "__main__":
    m = int(input().strip())
    arr = [ int (i) for i in input().strip().split()]
    result = insertion_sort(arr)
    print(" ".join(map(str,arr)))