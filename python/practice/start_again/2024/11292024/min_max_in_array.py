#  https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

# Solution - 01 
# def MinMax(arr):
#     print (min(arr), max(arr))

# Solution - 02
def Min(arr):
    res = arr[0]
    n = len(arr)
    for i in range(1, n ):
        res = min(res, arr[i])
    return res
def Max(arr):
    res = arr[0]
    n = len(arr)
    for i in range(1, n ):
        res = max(res, arr[i])
    return res

if __name__ == "__main__":
    arr = [3, 2, 1, 56, 10000, 167]
    # MinMax(arr)
    print ("Min number from list", Min(arr))
    print ("Max number from list", Max(arr))