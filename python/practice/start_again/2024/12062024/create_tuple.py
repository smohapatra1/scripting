#   https://www.geeksforgeeks.org/python-program-to-create-a-list-of-tuples-from-given-list-having-number-and-its-cube-in-each-tuple/

def Cube(list):
    res = [(val, pow(val, 3)) for val in list]
    return res

if __name__ == "__main__":
    list = [1, 2, 3]
    print ("Cube ", Cube(list))