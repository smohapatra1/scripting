#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def Inverted_Pyramid(n):
    for i in range(n, 0 , -1):
        for j in range(n-i):
            print (" ", end="")
        for k in range(2*i-1):
            print ("*", end="")
        print ("")

if __name__ == "__main__":
    n = 5 
    Inverted_Pyramid(n)