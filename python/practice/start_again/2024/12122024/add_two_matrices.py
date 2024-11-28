#   https://www.geeksforgeeks.org/python-program-add-two-matrices/

def Add(X,Y):
    result = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    for row in result:
        print (row)


if __name__ == "__main__":
    X = [[1, 2, 13],
        [4, 5, 6],
        [7, 8, 9]]

    Y = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]]
    Add(X, Y)