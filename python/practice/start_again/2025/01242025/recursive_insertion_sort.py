#   https://www.geeksforgeeks.org/python-program-for-recursive-insertion-sort/?ref=lbp

def InsertionRecursiveSort(A, n):
    if n <= 1:
        return
    # Sorting n-1 Elements
    InsertionRecursiveSort(A, n-1)
    last = A[n-1]
    j = n-2
    while j >=0 and A[j] > last:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = last

if __name__ == "__main__":
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    n = len(A)
    print ("Unsorted: ", A)
    InsertionRecursiveSort(A, n)
    print ("Sorted  : ", A)