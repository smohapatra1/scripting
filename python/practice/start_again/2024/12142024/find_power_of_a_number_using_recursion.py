# https://www.geeksforgeeks.org/python-program-to-find-the-power-of-a-number-using-recursion/

def Power(N, P):
    if P == 0:
        return 1 
    # return pow(N, P)
    return (N * Power(N, P-1))


if __name__ == "__main__":
    N = 2 
    P = 3 
    print (" ",Power(N, P ))