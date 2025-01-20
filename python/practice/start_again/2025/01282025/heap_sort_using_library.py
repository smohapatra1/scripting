#   https://www.geeksforgeeks.org/python-program-for-heap-sort/

import heapq

def HeapSort(arr):
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result


if __name__ == "__main__":
    arr = [60, 20, 40, 70, 30, 10]
    print ("Unsorted Array : ", arr)
    print ("Sorted Array   : ", HeapSort(arr))