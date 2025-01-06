#   https://www.geeksforgeeks.org/check-whether-an-array-is-subarray-of-another-array/

def search(a, b ):
    n = len(a)
    m = len(b)
    res = []
    for i in range(n - m +1 ):
        S = True
        for j in range(m):
            if a[i+j] != b[j]:
                S = False
                break
        if S :
            res.append(i)
    return res
if __name__ == "__main__":
    a = [2, 3, 0, 3, 0, 3, 0]
    b = [3, 0, 3, 0]
    a1 = [1, 2, 3, 4, 5]
    b1 = [2, 5, 6]
    res = search(a, b )
    res1 = search(a1, b1 )
    for idx in res:
        print (idx, end = ' ')
    for idx in res1:
        print (idx, end = ' ')