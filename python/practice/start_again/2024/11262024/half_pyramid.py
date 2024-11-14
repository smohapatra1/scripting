#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def halfpyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print ("*", end=" ")
        print ("")

if __name__ == "__main__":
    n = 5 
    halfpyramid(n)