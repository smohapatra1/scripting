#   https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/

def SmallestList(list):
    list.sort()
    return list[0]

if __name__ == "__main__":
    list = [ 10, 11, 14, 13, 12, 20, 1, 40 ]
    result = SmallestList(list)
    print (result)