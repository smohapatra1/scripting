# https://www.geeksforgeeks.org/python-program-to-print-negative-numbers-in-a-list/
def NegativeNum(n):
    res = [ ]
    for i in n:
        if i < 0:
            print (i, end=' ')

if __name__ == "__main__":
    n = [12, -7, 5, 64, -14]
    result = NegativeNum(n)