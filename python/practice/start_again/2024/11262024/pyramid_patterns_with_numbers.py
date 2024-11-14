#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def numpattern(n):
    num = 1 
    for i in range(0, n):
        num = 1 
        for j in range(0, i+1):
            print (num, end=" ")
            num = num + 1
        print ("")


if __name__ == "__main__":
    n = 5
    numpattern(n)