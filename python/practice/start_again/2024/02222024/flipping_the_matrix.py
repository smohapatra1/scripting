#   https://www.hackerrank.com/test/4nahpm20m33/questions/di1dm3kpigj


def flippingMatrix(matrix):
    n=len(matrix)
    total=0
    for i in range(n//2):
        for j in range(n//2):
            total +=max(matrix[i][j], matrix[i][n-j-1],matrix[n-i-1][j],matrix[n-i-1][n-j-1])
    return total

if __name__ == "__main__":
    q=int(input().strip())
    for _ in range(q):
        n=int(input().strip())  
        matrix=[]
        for _ in range(2*n):
            row=list(map(int, input().strip().split()))
            matrix.append(row)
        result=flippingMatrix(matrix)
        print (result)