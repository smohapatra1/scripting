#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/

def Pyramid(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print (" ", end="")
        for k in range(1, 2*i):
            print ("*", end="")
        print ()

if __name__ == "__main__":
    n = 5 
    Pyramid(n)