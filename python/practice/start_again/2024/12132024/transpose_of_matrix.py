#   https://www.geeksforgeeks.org/python-program-to-find-transpose-of-a-matrix/

def transpose(A, N ):
    res = [[row[i] for row in A] for i in range(len(A[0]))]
    print ("Original Matrix : ")
    for row in A:
        print (row)
    print ("Transport Matrix : ")
    for row in res:
        print (row)

if __name__ == "__main__":
    A = [ [1, 1, 1, 1], 
        [2, 2, 2, 2], 
        [3, 3, 3, 3], 
        [4, 4, 4, 4]] 
    N = 4 
    transpose(A, N )