#   https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/

def LargestList(list):
    list.sort()
    return list[-1]

if __name__ == "__main__":
    list = [ 10, 11, 14, 13, 12, 20, 1, 40 ]
    result = LargestList(list)
    print (result)