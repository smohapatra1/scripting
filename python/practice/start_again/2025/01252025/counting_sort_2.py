#   https://www.geeksforgeeks.org/python-program-for-counting-sort/

def countSort(arr):
    output = [ 0 for i in range(256)]
    count = [ 0 for i in range(256)]
    res = [ "" for _ in arr]
    for i in arr:
        count[ord(i)] += 1
    for i in range(256):
        count [i] += count[i-1]
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
    for i in range(len(arr)):
        res[i] = output[i]
    return res 

if __name__ == "__main__":
    arr = "geeksforgeeks"
    ans = countSort(arr)
    print ("Sorted character array is %s"  %("".join(ans)))