#   https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
def Swap(a):
    a[3], a[1] = a[1], a[3]
    return a

if __name__ == "__main__":
    a = [23, 65, 19, 90]
    print ("Current list = ", a)
    print ("After Swap   = ", Swap(a))