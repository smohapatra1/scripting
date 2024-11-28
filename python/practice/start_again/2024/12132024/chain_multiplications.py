#   https://www.geeksforgeeks.org/python-program-for-matrix-chain-multiplication-dp-8/

import sys

def MatrixChainOrder(arr):
    size = len(arr)
    m = [[0 for x in range(size)] for  x in range(size)]
    for i in range(1, size ):
        m[i][i] = 0 
    for L in range(2, size):
        for i in range(1, size-L+1):
            j = i + L -1
            m[i][j] = sys.maxsize
            for k in range(i, j ):
                q = m[i][k] + m[k + 1][j] + arr[i-1]*arr[k]*arr[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][size-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 3]
    print ("Minimum number of multiplications : ", MatrixChainOrder(arr))