#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def ReversePyramid(n):
    for i in range(n, 0, -1):
        print (' ' * (n-i) + '*' * (2*i-1))

if __name__ == "__main__":
    n = 10 
    ReversePyramid(n)