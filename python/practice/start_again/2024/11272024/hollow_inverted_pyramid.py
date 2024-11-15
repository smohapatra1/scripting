#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def Inverted_hollow_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print (" ", end="")
        for j in range(i):
            if j == 0 or j == i -1 or i == n:
                print ("*", end="")
            else:
                print (" ", end="")
        print ()

if __name__ == "__main__":
    n = 10
    Inverted_hollow_pyramid(n)