#   https://www.geeksforgeeks.org/python-merging-two-dictionaries/

def Merge(d1, d2):
    # Solution - 01 
    # d2.update(d1)
    # return d2
    # Solution - 02 
    d3 = {**d1 , **d2}
    return d3

if __name__ == "__main__":
    d1 = {'a': 10, 'b': 8}
    d2 = {'d': 6, 'c': 4}
    print ("values after merging : ", Merge(d1, d2))