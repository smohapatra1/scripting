#   https://www.geeksforgeeks.org/python-program-for-comb-sort/


def getNextGap(gap):
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return gap

def combSort(arr):
    n = len(arr)
 
    # Initialize gap
    gap = n
 
    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True
 
    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped == 1:
 
        # Find next gap
        gap = getNextGap(gap)
 
        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False
 
        # Compare all elements with current gap
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True


if __name__ == "__main__":
    arr = [8, 4, 1, 3, -44, 23, -6, 28, 0]
    print ("Original array:" , arr)
    combSort(arr)
    print ("Sorted array:", arr)