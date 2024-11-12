#   https://www.geeksforgeeks.org/problems/while-loop-in-python/1

def ReversedOrder(x):
    while x >= 0:
        print (x, end=" ")
        x -= 1
if __name__ == "__main__":
    x = 3
    ReversedOrder(x)
