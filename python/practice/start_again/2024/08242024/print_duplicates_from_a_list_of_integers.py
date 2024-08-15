#   https://www.geeksforgeeks.org/python-program-print-duplicates-list-integers/

def printDupe(n):
    # Solution - 01 
    # unique = []
    # duplicate = []
    # for i in n:
    #     if i not in unique:
    #         unique.append(i)
    #     elif i not in duplicate:
    #         duplicate.append(i)
    # return duplicate 
    # Solution - 02 
    res = []
    for i in n:
        a = n.count(i)
        if a > 1 :
            if res.count(i) == 0:
                res.append(i)
    return res


if __name__ == "__main__":
    n = [ 1, 4, 5, 2, 3, 1, 1, 3, 5, 4, 6]
    r = printDupe(n)
    print (r)