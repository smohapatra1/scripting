#   https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/

def PrintMatrix(R, C):
    res = [[int(input()) for x in range(C)] for y in range(R)]
    return res

if __name__ == "__main__":
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))
    print ("Matrix ", PrintMatrix(R, C ))