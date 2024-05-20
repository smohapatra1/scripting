#   How would you implement the insertion sort algorithm?

def InsertionSort(t):
    if len(t) <= 1:
        return 
    t.sort()
    for i in range(1, len(t)):
        j = i - 1 
        k = t[i]
        while (j>=0) and (t[j] > k):
            t[j+1] = t[j]
            j -= 1
            t[j+1] = k 

if __name__ == "__main__":
    t = [int (i) for i in input().strip().split()]
    result = InsertionSort(t)
    print (" ".join(map(str, t)))

