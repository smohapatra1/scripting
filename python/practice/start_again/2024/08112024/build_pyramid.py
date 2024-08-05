#   Building a Pyramid in Python

def Pyramid (n):
    h = 2 * n - 1
    for i in range(1, 2 * n , 2):
        print ('{:^{}}'.format('*'*i, h ))

if __name__ == "__main__":
    n = 5
    result = Pyramid(n)