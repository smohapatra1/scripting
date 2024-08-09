#   https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

def InterchangeNum(a):
    n = len(a)
    temp = a[0]
    a[0] = a [n-1]
    a[n-1] = temp
    return a 


if __name__ == "__main__":
    a = [12, 35, 9, 56, 24]
    result = InterchangeNum(a)
    print (result)