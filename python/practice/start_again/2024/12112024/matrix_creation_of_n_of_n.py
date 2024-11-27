#   https://www.geeksforgeeks.org/python-matrix-creation-of-nn/
import itertools

def NewMatrix(N):
    temp = itertools.count(1)
    res = [[next(temp) for i in range(N)] for i in range(N)]
    return res

if __name__ == "__main__":
    N = 4 
    print ("New Matrix : ", NewMatrix(N))