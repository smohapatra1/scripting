#   https://www.geeksforgeeks.org/python-program-multiply-two-matrices/

def Multiply(matrix_a, matrix_b):
    result = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = (matrix_a[i][0] * matrix_b[0][j] + matrix_a[i][1] * matrix_b[1][j])
    for row in result:
        print(row)

if __name__ == "__main__":
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    Multiply(matrix_a, matrix_b)