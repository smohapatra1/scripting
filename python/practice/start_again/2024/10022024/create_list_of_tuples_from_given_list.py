#   https://www.geeksforgeeks.org/python-program-to-create-a-list-of-tuples-from-given-list-having-number-and-its-cube-in-each-tuple/

def CTuple(list1):
    res = [ (val, pow(val, 3)) for val in list1]
    return res

if __name__ == "__main__":
    list1 = [1, 2, 5, 6]
    result = CTuple(list1)
    print (result)