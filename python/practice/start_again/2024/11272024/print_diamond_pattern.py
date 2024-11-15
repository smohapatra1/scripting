#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def Diamond(n):
    for i in range(n):
        print (' ' * (n-i-1) + '*' * (2*i+1))
    for i in range(n-2, -1, -1 ):
        print (' ' * (n-i-1) + '*' * (2*i+1))

if __name__ == "__main__":
    n = 5 
    Diamond(n)