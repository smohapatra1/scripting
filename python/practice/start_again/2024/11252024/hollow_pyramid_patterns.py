#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def HallowPyramid(n):
    for i in range(1, n+1):
        for j in range(1, 2*n):
            if j == n - i + 1 or j == n+i-1 or i == n:
                print ("*", end="")
            else:
                print (" ", end="")
        print () 

if __name__ == "__main__":
    n = 5 
    HallowPyramid(n)
