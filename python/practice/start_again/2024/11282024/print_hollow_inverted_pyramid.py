#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion
def InvertedHollowPyramid(n):
    for i in range(n, 0, -1):
        if i == n or i == 1:
            print ('*' * i )
        else:
            print ('*' + ' ' * (i-2) + '*')
if __name__ == "__main__":
    n = 10
    InvertedHollowPyramid(n) 