#   https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/

def RemoveOccur(n, item):
    # Solution - 01 
    # res = [ i for i in n if i !=item ]
    # return res 
    # Solution - 02 
    c = n.count(item)
    for i in range(c):
        n.remove(item)
    return n

if __name__ == "__main__":
    n = [ 1, 1, 2, 3, 4, 5, 1, 2, 1]
    item = 1 
    result = RemoveOccur(n, item)
    print (result)