#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion
def Triangle(n):
    for i in range(n):
        print ('*' * (i+1))

if __name__ == "__main__":
    n = 5
    Triangle(n)